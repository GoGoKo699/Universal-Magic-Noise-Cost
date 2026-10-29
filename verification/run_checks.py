"""Exact finite smoke tests for Universal Magic Noise Cost.

These test full instrument normalization, finite code syndrome counts,
polynomial multiplicity, buffer conditioning, and genus rounding. They do not
prove universal statements or reconstruct the imported decoder.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import comb

import numpy as np

I2=np.eye(2,dtype=object)
X=np.array([[0,1],[1,0]],dtype=object)
Z=np.array([[1,0],[0,-1]],dtype=object)
Hnum=np.array([[1,1],[1,-1]],dtype=object)

def kron(*items):
    m=np.array([[1]],dtype=object)
    for x in items:m=np.kron(m,x)
    return m

def cnot(n,control,target):
    result=np.zeros((2**n,2**n),dtype=object)
    for j in range(2**n):
        k=j^((1<<(n-target-1)) if j&(1<<(n-control-1)) else 0)
        result[k,j]=1
    return result

def check_instrument():
    id64=np.eye(64,dtype=object)
    x6=kron(*([X]*6));z6=kron(*([Z]*6))
    pnum=(id64-x6)@(id64-z6)  # Pi=pnum/4
    vnum=kron(Hnum,I2,I2)@cnot(3,0,2)@cnot(3,0,1)
    mats=[]
    for t,c in product((0,1),repeat=2):
        bt=np.array([[int(t==0),int(t==1)]],dtype=object)
        bx=np.array([[1,(-1)**c]],dtype=object)
        bnum=kron(bt,bt,bx,I2,I2,I2)
        rc=kron(*([X if t else I2]*3))@kron(*([Z if c else I2]*3))
        mats.append(vnum@rc@bnum@pnum)  # K=mats/8
    en=sum((m.T@m for m in mats),np.zeros((64,64),dtype=object))
    z12=kron(Z,Z,*([I2]*4))
    expected=8*(id64-x6)@(id64-z6)@(id64+z12)
    assert np.array_equal(en,expected)
    assert np.array_equal(en@en,64*en)
    assert int(np.trace(en))==64*8
    for m in mats:assert np.array_equal(m,mats[0]) or np.array_equal(m,-mats[0])
    target=np.array([1]*7+[-1],dtype=object)
    tw=sum((np.outer(target@m,target@m) for m in mats),np.zeros((64,64),dtype=object))
    w=np.zeros(64,dtype=object)
    for position in range(2,6):
        single=1<<(5-position)
        w[single]=1;w[single^63]=-1
    assert np.array_equal(tw,64*np.outer(w,w))
    return {"accepted_effect_rank":int(np.trace(en))//64,"corrected_branches":4}

GA=[[int(c) for c in row] for row in ("11100100","11011000","11111111")]
GB=[[int(c) for c in row] for row in ("11011000","10101010","11111111")]
GC=[[int(c) for c in row] for row in ("10101010","11100100","11111111")]
GEN=(GA,GB,GC)

def check_detector():
    for a,b,c in product(range(3),repeat=3):
        actual=sum(GA[a][j]*GB[b][j]*GC[c][j] for j in range(8))%2
        assert actual==int(a==b==c and a<2)
    for u,v,w in product(range(8),repeat=3):
        row=[]
        for word,g in zip((u,v,w),GEN):
            row.append([sum(((word>>r)&1)*g[r][j] for r in range(3))%2 for j in range(8)])
        phase=sum(row[0][j]*row[1][j]*row[2][j] for j in range(8))%2
        ideal=((u&1)*(v&1)*(w&1)+((u>>1)&1)*((v>>1)&1)*((w>>1)&1))%2
        assert phase==ideal
    counts={}
    for weight in (0,1,2):
        total=accepted=joint=retained=0
        for sites in combinations(range(8),weight):
            for labels in product(range(1,8),repeat=weight):
                total+=1;syn=0;bits=[[0]*3 for _ in range(2)]
                for pos,label in zip(sites,labels):
                    syn^=label
                    for d in range(3):
                        if label & (1<<(2-d)):
                            for r in range(2):bits[r][d]^=GEN[d][r][pos]
                if syn==0:
                    accepted+=1
                    joint+=bool(any(bits[0]) or any(bits[1]))
                    retained+=bool(any(bits[0]))
        counts[weight]=(total,accepted,joint,retained)
    assert counts[0]==(1,1,0,0)
    assert counts[1]==(56,0,0,0)
    assert counts[2]==(1372,196,184,148)
    return {"phase_identity_cases":512,"fault_counts":{str(k):v for k,v in counts.items()}}

def check_geometry():
    vals={}
    for d in range(1,9):
        v=sum(Q(comb(d,j)**2,comb(6*d,d+4*j)) for j in range(d+1))
        vals[d]=str(v)
        if d<5:
            # The sextic power has the d+1 monomials a^(5d-4j)b^(d+4j).
            powers=[d+4*j for j in range(d+1)]
            assert len(set(powers))==d+1 and min(powers)==d and max(powers)==5*d
    assert vals[1]=='1/3' and vals[2]=='8/231' and vals[3]=='2/663'
    assert Q(1,6**2*Q(8,231))==Q(77,96)
    return {"V_d":{str(k):v for k,v in vals.items()}}

def genus(i):
    return (33*32**(i-1)-34*32**((i-1)//2)+1 if i%2 else
            33*32**(i-1)-561*32**(i//2-1)+1)

def check_codes():
    B=67535825
    assert genus(3)==32705 and 2065*genus(3)==B
    for i in range(3,19):
        g=genus(i)
        assert 63*32**(i-1)<2*g<66*32**(i-1)
        assert genus(i+1)<34*g
    for d in (2,3,4088,4089,4090,132925,132926,4321025,4321026):
        i=3
        while genus(i)//8<d-1:i+=1
        g=genus(i)
        assert g//8>=d-1
        if i>3:
            assert genus(i-1)//8<d-1
            assert 2065*g<561680*(d-1)
        assert 2065*g<=B*d
    return {"first_genus":genus(3),"conservative_B":B}

def check_buffer():
    q,delta=Q(2,7),Q(3,11)
    weights={a:Q(0) for a in product('GB',repeat=2)}
    probs={'R':1-q,'G':q*(1-delta),'B':q*delta}
    good=Q(0)
    for outcomes in product('RGB',repeat=5):
        flags=tuple(c for c in outcomes if c!='R')
        if len(flags)<2:continue
        p=Q(1)
        for c in outcomes:p*=probs[c]
        good+=p;weights[flags[:2]]+=p
    assert good==Q(7432,16807)
    for pair,w in weights.items():
        expected=delta**pair.count('B')*(1-delta)**pair.count('G')
        assert w/good==expected
    return {"buffer_success":str(good),"retained_conditional":{''.join(k):str(v/good) for k,v in weights.items()}}

def main():
    for label,fn in [('full_concentration_instrument',check_instrument),
                     ('eight_CCZ_detector',check_detector),('symmetric_geometry',check_geometry),
                     ('code_rounding',check_codes),('buffer_conditioning',check_buffer)]:
        result=fn()
        print('PASS',label,result)
    print('All exact finite checks passed; analytical theorems require the written proofs.')
if __name__=='__main__':main()
