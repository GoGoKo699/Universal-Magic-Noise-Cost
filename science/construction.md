# Construction: buffered universal concentration and correcting CCZ distillation

This is the upper bound of [T1](results.md), with every failed and discarded raw input counted. Both the inner six-copy concentration and the outer correcting code are inherited primitives; the new resource statement follows from their uniform yield, conditioning, and all-integer-order accounting.

## 1. Six-copy exact concentration

Take the Rizzo–Leone successful six-copy map $`\mathcal E_6`$, with every accepted branch Clifford corrected into the fixed CCZ target. On an ideal pure input of unit Bloch vector $`(x,y,z)`$,

```math
\mathcal E_6(\psi^{\otimes6})=q_\psi(0)\tau,\quad
q_\psi(0)=\frac{1-x^6-y^6-z^6}{6}
=\frac{M_3^{\mathrm{lin}}(\psi)}3.
\qquad\text{(U1)}
```

Put $`a=\max\{|x|,|y|,|z|\}=1-2\eta`$. Since $`x^2+y^2+z^2=1`$,

```math
a^6\le x^6+y^6+z^6\le a^4,
\quad\Rightarrow\quad \frac{\eta}{3}\le q_\psi(0)\le2\eta.
\qquad\text{(U2)}
```

For the noisy input, define $`q_\psi(p)=\mathrm{Tr}\mathcal E_6(\rho_\psi(p)^{\otimes6})`$, normalized accepted state $`\sigma_\psi(p)`$, and accepted infidelity $`\delta_\psi(p)=1-\mathrm{Tr}[\tau\sigma_\psi(p)]`$. The all-ideal tensor term in $`\rho_\psi(p)^{\otimes6}`$ has weight $`(1-p)^6`$. Completely positive trace-nonincreasing processing gives

```math
q_\psi(p)\ge(1-p)^6 q_\psi(0),\qquad
q_\psi(p)\delta_\psi(p)\le1-(1-p)^6.
\qquad\text{(U3)}
```

The second inequality counts all outcomes containing at least one replacement. It does not assume that the noisy accepted output is depolarizing or symmetric. Hence for $`0\le p\le1/12`$,

```math
q_\psi(p)\ge\eta/6,\qquad
\delta_\psi(p)\le\min\{1,36p/\eta\}.
\qquad\text{(U4)}
```

## 2. Free twirls for arbitrary accepted errors

For $`C=\mathrm{CCZ}`$, the operators $`g_s=CX^sC^\dagger`$ ($`s\in\mathbb F_2^3`$) are Cliffords: e.g. $`g_{100}=X_1\mathrm{CZ}_{23}`$. Their random application dephases any CCZ-register density matrix in the orthonormal basis $`|c_e\rangle=Z^e|\mathrm{CCZ}\rangle`$, without changing target fidelity:

```math
\mathcal T_{\mathrm{CCZ}}(\sigma)=\tfrac18\sum_s g_s\sigma g_s^\dagger
=\sum_{e\in\mathbb F_2^3}r_e|c_e\rangle\langle c_e|,
\quad r_0=1-\delta_\psi(p).
\qquad\text{(U5)}
```

The algebraic appearance of $`C`$ is not an instruction to supply a non-Clifford gate for free: each $`g_s`$ has a direct Clifford circuit.

The Wills–Hsieh–Yamasaki qudit protocol similarly has free conjugated-shift twirls in its fixed ten-qubit representation. They reduce arbitrary correlated errors supported on specified faulty qudit sites to a mixture of Pauli $`Z`$ patterns supported on those sites. The code corrects all such patterns up to its decoding radius.

## 3. An outer correction map for every integer order

For each $`d\ge1`$, construct a deterministic stabilizer channel $`\mathcal D_d`$ which consumes $`m_d`$ CCZ resources and returns at least one CCZ, correcting exactly every pattern in which fewer than $`d`$ entire CCZ input registers have arbitrary faults. The identity gives $`m_1=1`$. For $`d\ge2`$, invoke the inherited code and conversion of [Wills, Hsieh and Yamasaki](../references/RELATED_WORK.md#constant-overhead-correction), specifically arXiv:2408.07764v2 §§4.2, 4.4, Example 5.3.1, §6, Appendix B.

The code over $`\mathbb F_{1024}`$ has length $`N_i\lt (59/2)g_i`$ and corrects up to $`t_i=\lfloor g_i/8\rfloor`$ faulty qudits, with $`K_i=\lfloor5g_i/4\rfloor`$ outputs. One fixed preparation decomposes its ten-qubit non-Clifford resource into $`C=70`$ CCZ injections, with no additional supplied magic. Thus $`70N_i`$ CCZ resources prepare the $`N_i`$ code inputs; one erroneous raw CCZ can contaminate only its own preparation group. Per-qudit twirling followed by the published decoder corrects every fault set of size at most $`t_i`$. The decoder is unconditional; unused output CCZs can be discarded.

The source's explicit algebraic-geometry genus sequence, for $`i\ge3`$, is

```math
g_i=
\begin{cases}
33\cdot32^{i-1}-34\cdot32^{(i-1)/2}+1,&i\ \mathrm{odd},\\
33\cdot32^{i-1}-561\cdot32^{i/2-1}+1,&i\ \mathrm{even}.
\end{cases}
\qquad\text{(U6)}
```

It obeys $`g_3=32705`$, $`(63/2)32^{i-1}\lt g_i\lt 33\cdot32^{i-1}`$, and $`g_{i+1}/g_i\lt 34`$. For any integer $`d\ge2`$, choose the first $`i\ge3`$ with $`t_i\ge d-1`$, then $`m_d=70N_i\lt 2065g_i`$. If $`i>3`$, minimality gives $`g_{i-1}\lt 8(d-1)`$, hence $`m_d\lt 561680(d-1)`$. In the initial case $`m_d\lt 2065\cdot32705=67535825`$. Therefore the one constant

```math
B=67535825,\qquad m_d\le Bd
\qquad\text{(U7)}
```

works for every positive integer $`d`$. This explicit spacing step cannot be inferred from the phrase “asymptotically good code” alone. Its constants are sufficient, not practical thresholds or optimized overhead.

## 4. Buffering, conditioning and raw inputs

For fixed design parameters $`d,\eta_0,\alpha`$, run $`L`$ independent six-copy concentration attempts on disjoint raw inputs. If fewer than $`m_d`$ succeed, report failure; otherwise retain the first $`m_d`$ successes, apply the Clifford CCZ twirl, and execute $`\mathcal D_d`$. Every run consumes at most $`n=6L`$ raw inputs.

The accepted state of each independent concentration trial is the same $`\sigma_\psi(p)`$, regardless of fine correction labels after those corrections are performed. Conditioning on any full pattern of binary success flags leaves the accepted outputs as a tensor product of $`\sigma_\psi(p)`$. Selecting the first $`m_d`$ successes preserves that product upon mixing flag patterns. Thus the outer code receives precisely $`m_d`$ independent copies of the (possibly anisotropic) accepted state, not an assumed depolarized state.

Set $`h_\alpha=\ln[1/(1-\alpha)]`$ and choose

```math
L=\left\lceil\frac{12m_d+48h_\alpha}{\eta_0}\right\rceil.
\qquad\text{(U8)}
```

For $`\eta(\psi)\ge\eta_0`$ and $`0\le p\le1/12`$, (U4) gives binomial success count mean $`\mu=Lq_\psi(p)\ge2m_d+8h_\alpha`$. The multiplicative Chernoff bound yields

```math
1-S_\psi(p)\le\Pr\{\mathrm{Bin}(L,q_\psi(p))\le\mu/2\}
\le e^{-\mu/8}\le1-\alpha.
\qquad\text{(U9)}
```

At $`p=0`$, every concentration success gives exact CCZ. The buffering protocol therefore returns exact CCZ and has positive ideal success for all nonstabilizer directions, even those outside the distance promise. No measurement outcome or circuit gate depends on $`\psi`$ or $`p`$.

## 5. Finite-noise suppression

After twirling, each selected output has error probability $`\delta_\psi(p)`$, independently of the others. $`\mathcal D_d`$ corrects every pattern of fewer than $`d`$ faulty resources; thus

```math
e_\psi(p)\le
\Pr\{\mathrm{Bin}(m_d,\delta_\psi(p))\ge d\}
\le \binom{m_d}d\delta_\psi(p)^d
\le \left(36eB\,p/\eta(\psi)\right)^d.
\qquad\text{(U10)}
```

The union bound over $`d`$-subsets is valid even when the right-hand side exceeds one. In particular every fixed nonstabilizer direction has order $`d`$ error. Uniformly for $`\eta(\psi)\ge\eta_0`$ and $`0\le p\le\eta_0/(72eB)`$, the error is at most $`2^{-d}`$ and success is at least $`\alpha`$.

The maximum raw-copy budget is

```math
n=6L\le6+\frac{72Bd+288h_\alpha}{\eta_0}
=O_\alpha(d/\eta_0).
\qquad\text{(U11)}
```

This proves the constructive half of T1. No better practical constant, physical circuit cost, or optimal noise threshold is claimed.

## 6. Correct scope of the inherited operations

The code, decoding theorem, ten-qubit/CCZ conversion and six-copy conversion are not new. The construction supplies the matching result in the unknown-source task, including the difficulty of a state-dependent inner acceptance probability. All nonfree inputs are charged. No catalytic T-state conversion in the correcting-code paper is used. The construction does not give a constant-success 48-input quadratic protocol: that finite example has a very small yield and fulfills a different role.
