# Explicit 48-copy quadratic factory

The general [joint law](results.md) uses a buffered construction with large existence constants. This page instead specifies a small, fixed **order-two** witness: eight independent six-copy universal concentration attempts followed by an inherited eight-to-two CCZ error detector. Keep the first output when accepted. The maximum consumed input is 48 raw qubits; ideal success is positive for every nonstabilizer pure direction, though not bounded uniformly as the direction approaches a stabilizer ray.

## Full six-qubit concentration instrument

Use the Rizzo–Leone Pauli-syndrome projector

$$
\Pi=\tfrac14(I-X^{\otimes6})(I-Z^{\otimes6}).
$$

Both commuting Pauli measurements must yield eigenvalue \(-1\). Measure qubits 1 and 2 in the computational basis and accept only equal results \(t,t\); measure qubit 3 in the \(X\)-basis with outcome \(c\). Define

$$
|x_c\rangle=(|0\rangle+(-1)^c|1\rangle)/\sqrt2,\quad
B_{tc}=\langle t,t,x_c|\otimes I_8,
$$

$$
R_{tc}=(X^{\otimes3})^t(Z^{\otimes3})^c,\quad
V=H_1\,\mathrm{CNOT}_{1\to3}\mathrm{CNOT}_{1\to2},
\quad K_{tc}=V R_{tc}B_{tc}\Pi.
\tag{F1}
$$

The four corrected accepted branches produce the trace-nonincreasing map \(\mathcal E_6(\omega)=\sum_{t,c}K_{tc}\omega K_{tc}^\dagger\). The full projector has rank 16; its restriction to identical pure symmetric inputs is a rank-one line, *but that replacement is invalid when evaluating independent depolarizing noise*.

The acceptance effect and the target-weight effect obey

$$
\sum_{t,c}K_{tc}^\dagger K_{tc}
=\tfrac18(I-X^{\otimes6})(I-Z^{\otimes6})(I+Z_1Z_2),
\tag{F2}
$$

$$
\sum_{t,c}K_{tc}^\dagger\tau K_{tc}=|w\rangle\langle w|,
\quad
|w\rangle=2^{-3/2}\sum_{j=3}^{6}(|1_j\rangle-|\overline{1_j}\rangle).
\tag{F3}
$$

Here \(|1_j\rangle\) is the computational six-bit string with a single 1 at position \(j\), and the bar complements every bit. For an ideal \(\psi=a|0\rangle+b|1\rangle\),

$$
q_\psi(0)=2|ab(a^4-b^4)|^2
=\tfrac16(1-x^6-y^6-z^6).
\tag{F4}
$$

The same operation on \(\rho_\psi(p)^{\otimes6}\) has an arbitrary accepted output, not necessarily a uniform mixture of seven CCZ errors. We twirl it by free Clifford conjugated shifts, as in [the construction](construction.md#2-free-twirls-for-arbitrary-accepted-errors). The result is diagonal in the CCZ-error basis \(Z^e|\mathrm{CCZ}\rangle\), \(e\in\mathbb F_2^3\).

## Eight-to-two CCZ detector

Use the three binary matrices of [Chamberland et al., Appendix O](../references/RELATED_WORK.md#the-eight-ccz-detector), with rows 1–2 representing logical output qubits and row 3 the syndrome:

$$
G_A=\begin{pmatrix}1&1&1&0&0&1&0&0\\1&1&0&1&1&0&0&0\\1&1&1&1&1&1&1&1\end{pmatrix},\quad
G_B=\begin{pmatrix}1&1&0&1&1&0&0&0\\1&0&1&0&1&0&1&0\\1&1&1&1&1&1&1&1\end{pmatrix},
$$

$$
G_C=\begin{pmatrix}1&0&1&0&1&0&1&0\\1&1&1&0&0&1&0&0\\1&1&1&1&1&1&1&1\end{pmatrix}.
\tag{F5}
$$

All arithmetic in these matrices is over \(\mathbb F_2\). For each of eight resource qudits, couple auxiliary plus-state qubits to its three physical qubits using CNOTs controlled by the corresponding matrix entries, measure the used resource in the computational basis, and apply the resulting *Clifford* diagonal phase correction. The correction is Clifford because the cubic product of the three mod-2 linear forms cancels in the difference between the observed and ideal cubic phases; the remaining terms are degree at most two and are \(Z\)/\(CZ\) corrections. The final check qubits \((A,3),(B,3),(C,3)\) are measured in the \(X\) basis, accepting only three \(+1\) results. The six remaining auxiliaries hold two CCZ outputs. A circuit-level presentation appears in the cited paper (Fig. 60 and Algorithm 2).

For CCZ-basis input error labels \(e_j=(e_{A,j},e_{B,j},e_{C,j})\), acceptance means

$$
v_D=\sum_{j=1}^8 e_{D,j}=0,\quad D\in\{A,B,C\},
\tag{F6}
$$

and accepted output \(r=1,2\) has CCZ error bits

$$
u_{D,r}=\sum_{j=1}^8G_D[r,j]\,e_{D,j}.
\tag{F7}
$$

An error on a single input resource has nonzero three-bit syndrome and is always rejected. Hence every accepted harmful event contains faults on at least two of the eight CCZ inputs. There are \(\binom82\cdot7^2=1372\) labelled two-fault configurations. Exact enumeration gives 196 accepted, 184 harmful to at least one output, and 148 harmful to the **first retained output**. Those different counts are essential; the first-output error is not half the joint error.

## Whole factory and analytical order-two guarantee

Apply the concentration instrument independently to eight disjoint groups. Report failure unless all eight succeed. Twirl each of the eight accepted resources, run the detector, and keep the first logical output only if the three checks accept. If \(\delta_\psi(p)\) is the single accepted concentration output infidelity, detector success is at least \([1-\delta_\psi(p)]^8\), and its retained-output error numerator is at most \(\binom82\delta_\psi(p)^2\). Therefore

$$
e_\psi(p)\le
\frac{28\delta_\psi(p)^2}{(1-\delta_\psi(p))^8}=O_\psi(p^2).
\tag{F8}
$$

Alternatively, in the positive tensor expansion of the 48 raw inputs, a harmful accepted output requires at least two depolarizing replacements, since the outer detector eliminates the only potentially wrong CCZ error from any single affected group. Thus

$$
S_\psi(p)\ge(1-p)^{48}q_\psi(0)^8,\quad
S_\psi(p)e_\psi(p)\le \binom{48}{2}p^2.
\tag{F9}
$$

This proves order two for every pure nonstabilizer \(\psi\) without assuming the conditional error labels are equiprobable. The ideal success is

$$
S_\psi(0)=q_\psi(0)^8>0.
\tag{F10}
$$

## A generic exact example and its error convention

Take

$$
|\psi\rangle=[2|0\rangle+(1+i)|1\rangle]/\sqrt6,\quad
(x,y,z)=(2/3,2/3,1/3),\quad\eta=1/6.
$$

For \(r=1-p\), evaluating (F1) on the *full* six-qubit noisy tensor state yields

$$
q_\psi(p)=\frac{729+81r^2-9r^4-r^6}{5832},\qquad
g_\psi(p)=\frac{729+2349r^2+2979r^4+343r^6}{46656},
\tag{F11}
$$

where \(g_\psi\) is the unnormalized overlap with \(\tau\). Both at \(p=0\) equal \(100/729\), and the accepted concentration infidelity is

$$
\delta_\psi(p)=1-g_\psi(p)/q_\psi(p)
=\frac{1107}{400}p+O(p^2).
\tag{F12}
$$

Exact convolution of all eight anisotropic CCZ-error distributions through the detector gives

$$
\boxed{e_\psi(p)=\frac{616167}{20000}p^2+O(p^3)}
\tag{F13}
$$

for **the first retained output**. The *joint* two-output infidelity instead has coefficient \(1679859/40000\). At zero noise \(S_\psi(0)=(100/729)^8\approx1.254\times10^{-7}\).

The full probability polynomials, finite syndrome counts and exact numerical checks are the objects of [verification](../verification/README.md). This low-yield 48-copy witness is not claimed to be an optimal constant-yield factory or the minimal order-two circuit; the converse only requires at least \(n=12\) copies.
