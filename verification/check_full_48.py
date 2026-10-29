"""Exact all-48-input polynomial from the full six-copy instrument and detector.

This is slower than run_checks.py because it propagates exact integer
coefficients through the 64-state outer detector transfer map.
"""
from fractions import Fraction as Q
from itertools import combinations,product
import numpy as np
import run_checks as base

def concentration_kraus():
    I=base.I2;X=base.X;Z=base.Z;H=base.Hnum
    ident=np.eye(64,dtype=object)
    projector=(ident-base.kron(*([X]*6)))@(ident-base.kron(*([Z]*6)))
    u=base.kron(H,I,I)@base.cnot(3,0,2)@base.cnot(3,0,1)
    mats=[]
    for t,c in product((0,1),repeat=2):
        bt=np.array([[int(t==0),int(t==1)]],dtype=object)
        bx=np.array([[1,(-1)**c]],dtype=object)
        b=base.kron(bt,bt,bx,I,I,I)
        r=base.kron(*([X if t else I]*3))@base.kron(*([Z if c else I]*3))
        mats.append(u@r@b@projector)
    return mats  # K_num = 8*K

def rho_power_polynomials():
    a_re=np.array([[4,2],[2,2]],dtype=object)
    a_im=np.array([[0,-2],[2,0]],dtype=object)
    b_re,b_im=3*base.I2-a_re,-a_im
    coeffs=[(np.array([[1]],dtype=object),np.array([[0]],dtype=object))]
    for i in range(6):
        d=2**(i+1)
        new=[(np.zeros((d,d),dtype=object),np.zeros((d,d),dtype=object)) for _ in range(len(coeffs)+1)]
        for j,(r,im) in enumerate(coeffs):
            for k,(s,si) in enumerate(((a_re,a_im),(b_re,b_im))):
                nr,ni=new[j+k]
                nr+=np.kron(r,s)-np.kron(im,si)
                ni+=np.kron(r,si)+np.kron(im,s)
        coeffs=new
    return coeffs

def poly_eval(poly,x):
    out=0
    for coefficient in reversed(poly):out=out*x+coefficient
    return out

def concentration_labels():
    mats=concentration_kraus();rho_coeffs=rho_power_polynomials()
    denom=8*64*6**6
    labels=[];raw=[]
    cc=np.array([1]*7+[-1],dtype=object)
    for e in range(8):
        v=np.array([cc[j]*(-1)**((j&e).bit_count()%2) for j in range(8)],dtype=object)
        rows=[v@m for m in mats]
        nums=[]
        for re,im in rho_coeffs:
            n=sum(int(row@re@row) for row in rows)
            assert sum(int(row@im@row) for row in rows)==0
            nums.append(n)
        raw.append(nums);labels.append([Q(n,denom) for n in nums])
    q=[sum(label[k] for label in labels) for k in range(7)]
    good=labels[0]
    assert q[0]==good[0]==Q(100,729)
    assert (q[1]-good[1])/q[0]==Q(1107,400)
    assert poly_eval(q,Q(1))==Q(1,8)
    assert all(poly_eval(label,Q(1))==Q(1,64) for label in labels)
    assert all(label[0]==0 for label in labels[1:])
    return labels,raw,denom,q,good

def retained_increment(site,label):
    x=0
    for d,g in enumerate(base.GEN):
        if label&(1<<(2-d)):
            x ^= g[0][site]<<d
    return x

def joint_increment(site,label):
    x=0
    for d,g in enumerate(base.GEN):
        if label&(1<<(2-d)):
            for r in range(2):x ^= g[r][site]<<(2*d+r)
    return x

def convolution(a,b):
    result=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):result[i+j]+=x*y
    return result

def run():
    labels,raw,denom,q,good=concentration_labels()
    states={(0,0):[1]}
    for site in range(8):
        new={}
        for (syn,out),pol in states.items():
            for e,epol in enumerate(raw):
                key=(syn^e,out^retained_increment(site,e))
                term=convolution(pol,epol)
                if key not in new:new[key]=[0]*len(term)
                for j,n in enumerate(term):new[key][j]+=n
        states=new
    acc=[0]*49
    for (syn,out),pol in states.items():
        if syn==0:
            for j,n in enumerate(pol):acc[j]+=n
    retained_good=states[(0,0)]
    error=[a-b for a,b in zip(acc,retained_good)]
    assert error[0]==error[1]==0 and error[2]>0
    assert Q(acc[0],denom**8)==Q(100,729)**8
    retained=Q(error[2],acc[0]);assert retained==Q(616167,20000)
    weighted_kept=Q(0);weighted_joint=Q(0)
    for label in range(1,8):
        harm_kept=harm_joint=0
        for a,b in combinations(range(8),2):
            harm_kept+=bool(retained_increment(a,label)^retained_increment(b,label))
            harm_joint+=bool(joint_increment(a,label)^joint_increment(b,label))
        v=labels[label][1]/q[0]
        weighted_kept+=harm_kept*v*v
        weighted_joint+=harm_joint*v*v
    assert weighted_kept==retained
    assert weighted_joint==Q(1679859,40000)
    assert Q(poly_eval(acc,1),denom**8)==Q(1,8)**9
    for p in (Q(1,10000),Q(1,1000),Q(1,100)):
        success=Q(poly_eval(acc,p),denom**8)
        err=Q(poly_eval(error,p),poly_eval(acc,p))
        assert 0<success<1 and 0<err<1
    return {'zero_noise_success':str(Q(acc[0],denom**8)),
            'accepted_concentration_infidelity_linear':str((q[1]-good[1])/q[0]),
            'retained_quadratic':str(retained),'joint_quadratic':str(weighted_joint),
            'degree':len(acc)-1}

if __name__=='__main__':print('PASS full_48',run())
