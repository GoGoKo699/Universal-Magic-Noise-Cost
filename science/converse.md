# Converse: universal robustness forces a kernel

This section proves the two complementary lower bounds in [T1](results.md): a universal success envelope depending on the free-state distance, and an algebraic obstruction proportional to the suppression order. The accepted map $`\Lambda`$ is fixed independently of $`\psi,p`$, completely positive, trace nonincreasing, and stabilizer-cone preserving. A fixed pure CCZ target is required on all ideal nonstabilizer inputs, together with conditional error $`O_\psi(p^d)`$.

## T2. Full low-excitation kernel and binomial yield envelope

For a pure one-qubit stabilizer ray $`|s\rangle`$, write $`|s_\perp\rangle`$ for its orthogonal stabilizer ray. Let $`|s;A\rangle`$ be the $`n`$-fold product equal to $`|s_\perp\rangle`$ on sites in $`A\subseteq[n]`$ and $`|s\rangle`$ otherwise. Define

```math
\mathcal S_{n,d}=\mathrm{span}\{|s;A\rangle:s\in\mathrm{Stab}_1,\;|A|\lt d\}.
\qquad\text{(C1)}
```

**Theorem T2.** Every Kraus operator $`K_j`$ in any decomposition of the accepted map annihilates $`\mathcal S_{n,d}`$. Consequently its acceptance effect $`E=\Lambda^*(I)`$ satisfies

```math
0\le E\le I-\Pi_{\mathcal S_{n,d}}.
\qquad\text{(C2)}
```

For any pure input $`\psi`$ and any stabilizer ray $`s`$, set $`\eta_s=1-|\langle s|\psi\rangle|^2`$. Then

```math
\boxed{S_\psi(0)\le
\sum_{k=d}^{n-d}\binom nk \eta_s^k(1-\eta_s)^{n-k}.}
\qquad\text{(C3)}
```

Take $`s`$ nearest to $`\psi`$, so $`\eta_s=\eta(\psi)`$. Markov's inequality and a union bound give

```math
S_\psi(0)\le
\Pr\{\mathrm{Bin}(n,\eta)\ge d\}
\le \min\{n\eta/d,\ \binom nd\eta^d\}.
\qquad\text{(C4)}
```

The empty sum is zero. These bounds apply to all accepted branches, with no restriction to permutation-symmetric implementations.

### Proof: positive fault sectors

Let $`\mathcal P_n=\{I,X,Y,Z\}^{\otimes n}`$, and $`w(P)`$ count nonidentity factors. Independent depolarization has the positive expansion

```math
\rho_\psi(p)^{\otimes n}=
\sum_{P\in\mathcal P_n}
(1-3p/4)^{n-w(P)}(p/4)^{w(P)}P\psi^{\otimes n}P.
\qquad\text{(C5)}
```

Define the nonnegative unnormalized damage of pattern $`P`$:

```math
h_P(\psi)=\mathrm{Tr}[(I-\tau)\Lambda(P\psi^{\otimes n}P)]\ge0.
```

The sum $`H_\psi(p)=\sum_P(1-3p/4)^{n-w(P)}(p/4)^{w(P)}h_P(\psi)`$ equals $`S_\psi(p)e_\psi(p)`$, hence is $`O_\psi(p^d)`$. Each summand is nonnegative for small positive $`p`$. Holding any pattern with $`w(P)\lt d`$ fixed and dividing its contribution by $`p^{w(P)}`$ yields $`h_P(\psi)=0`$. No cancellation can hide a harmful lower-weight pattern.

For any accepted Kraus representation,

```math
h_P(\psi)=\sum_j\|(I-\tau)K_jP|\psi\rangle^{\otimes n}\|^2.
```

Thus every accepted lower-weight error vector has output on the pure target line or is rejected. This holds for all nonstabilizer directions. The expression is continuous in $`\psi`$, so the zero-damage identity extends to every stabilizer ray $`s`$, without needing a uniform implicit constant in the error estimate near that ray.

At a stabilizer ray, $`P|s\rangle^{\otimes n}`$ is a stabilizer product state. Its accepted output cannot be a nonzero multiple of $`\tau`$, because $`\Lambda`$ preserves the stabilizer cone and $`\tau`$ is nonstabilizer. Therefore the accepted output is zero. By positivity,

```math
K_jP|s\rangle^{\otimes n}=0 \quad
\text{for every } j,\ s\in\mathrm{Stab}_1,\ w(P)\lt d.
\qquad\text{(C6)}
```

A suitable one-qubit Pauli switches $`s`$ and $`s_\perp`$ on each selected site. Hence (C6) is precisely the annihilation of (C1). Since $`E=\sum_jK_j^\dagger K_j\le I`$, this proves (C2).

### Proof: binomial projection

Expand an arbitrary $`|\psi\rangle`$ in the orthonormal basis $`(|s\rangle,|s_\perp\rangle)`$:

```math
|\psi\rangle=\sqrt{1-\eta_s}|s\rangle+
e^{i\phi}\sqrt{\eta_s}|s_\perp\rangle.
```

The tensor-power expansion has mutually orthogonal basis vectors indexed by subsets $`A`$, with squared amplitudes $`(1-\eta_s)^{n-|A|}\eta_s^{|A|}`$. By (C6), the effect $`E`$ annihilates every term with $`|A|\lt d`$. Repeating the same argument around $`s_\perp`$ also annihilates $`|A|>n-d`$. Trace nonincrease bounds acceptance by the total surviving weight, giving (C3). Markov's inequality for $`\mathrm{Bin}(n,\eta)`$ gives $`S_\psi(0)\le n\eta/d`$; a union bound over all $`d`$-subsets gives $`S_\psi(0)\le\binom nd\eta^d`$. This proves T2.

Every $`\eta_0`$ between zero and $`\eta_{\max}`$ occurs for some pure direction. Testing its required success floor $`\alpha`$ in (C4) yields

```math
\boxed{n\ge\alpha d/\eta_0.}
\qquad\text{(C7)}
```

## T3. Six-root multiplicity

**Theorem T3.** For any accepted Kraus operator $`K_j`$, its restriction to ideal pure tensor inputs is

```math
K_j(a|0\rangle+b|1\rangle)^{\otimes n}
=[ab(a^4-b^4)]^d q_j(a,b)\,|\mathrm{CCZ}\rangle,
\qquad\text{(C8)}
```

for a homogeneous polynomial $`q_j`$ of degree $`n-6d`$, unless the entire amplitude vanishes. Since ideal success is positive at every nonstabilizer ray, at least one polynomial is nonzero, and

```math
\boxed{n\ge6d.}
\qquad\text{(C9)}
```

**Proof.** Exactness of the sum of rank-one target outputs implies that each accepted Kraus vector on $`|\psi\rangle^{\otimes n}`$ lies on the target line. Its scalar coefficient $`c_j(a,b)`$ is a homogeneous holomorphic polynomial of degree $`n`$. For any pure stabilizer ray $`s`$, use local projective coordinates $`|s\rangle+t|s_\perp\rangle`$. Its $`n`$-fold tensor product is a polynomial in $`t`$ whose coefficient of $`t^r`$ is the sum of all $`|s;A\rangle`$ with $`|A|=r`$. Equation (C6) kills every coefficient with $`r\lt d`$. Thus $`c_j`$ has a zero of multiplicity at least $`d`$ at $`s`$.

The six stabilizer rays in coordinates $`[a:b]`$ are $`[1:0],[0:1],[1:\pm1],[1:\pm i]`$. Their pairwise relatively prime linear factors multiply, up to a nonzero scalar, to $`f_6(a,b)=ab(a^4-b^4)`$. Multiplicity $`d`$ at all six points implies $`f_6^d\mid c_j`$. Since a nonzero amplitude has degree $`n`$, $`n\ge6d`$. Taking squared Kraus norms also gives

```math
S_\psi(0)=|f_6(a,b)|^{2d}\sum_j |q_j(a,b)|^2.
\qquad\text{(C10)}
```

At $`n=6d`$, each nonzero $`q_j`$ is constant. Thus any such factory would have ideal yield proportional to $`[M_3^{\mathrm{lin}}(\psi)]^d`$. This necessary shape is not a construction.

The degree-six single-root ideal and exact six-copy pure-input conversion were previously identified by [Rizzo–Leone](../references/RELATED_WORK.md#universal-pure-input-concentration). The added multiplicity comes from suppressing all independent errors around all six directions, using the full input-space kernel.

## T4. Symmetric projection envelope

Let $`\mathcal H_{n,d}=\mathrm{Sym}^n(\mathbb C^2)\cap\mathcal S_{n,d}^{\perp}`$. Because $`\mathcal S_{n,d}`$ is invariant under input permutations, its projector commutes with the symmetric-subspace projector. Therefore

```math
S_\psi(0)\le\|\Pi_{\mathcal H_{n,d}}|\psi\rangle^{\otimes n}\|^2.
\qquad\text{(C11)}
```

To find its dimension, identify a symmetric vector $`v=\sum_{k=0}^n v_k|D_k^n\rangle`$ with homogeneous polynomial $`F_v(a,b)=\sum_k\bar v_k\sqrt{\binom nk}a^{n-k}b^k`$. Orthogonality to $`\mathcal S_{n,d}`$ is equivalent to a zero of multiplicity at least $`d`$ at each stabilizer ray, hence $`F_v\in f_6^d\,\mathbb C[a,b]_{n-6d}`$. Thus

```math
\dim\mathcal H_{n,d}=\max\{n-6d+1,0\}.
\qquad\text{(C12)}
```

At the algebraic minimum $`n=6d`$, define

```math
|v_d\rangle=\sum_{j=0}^{d}
\frac{(-1)^j\binom dj}{\sqrt{\binom{6d}{d+4j}}}|D_{d+4j}^{6d}\rangle,
\quad
V_d=\sum_{j=0}^{d}\frac{\binom dj^2}{\binom{6d}{d+4j}}.
```

Then $`\langle v_d|\psi^{\otimes6d}\rangle=f_6(a,b)^d`$, so the one-dimensional projection gives

```math
S_\psi(0)\le |f_6(a,b)|^{2d}/V_d
=\frac{[M_3^{\mathrm{lin}}(\psi)]^d}{6^dV_d}.
\qquad\text{(C13)}
```

For example $`V_1=1/3`$ and $`V_2=8/231`$, hence at $`n=12,d=2`$, $`S_\psi(0)\le(77/96)[M_3^{\mathrm{lin}}(\psi)]^2`$. At $`d=1`$, the geometric envelope is $`M_3^{\mathrm{lin}}/2`$, greater than the actual optimal six-copy stabilizer yield $`M_3^{\mathrm{lin}}/3`$. The projection is only a necessary condition; it is not itself a free physical effect.

## Boundary

The converse needs a single fixed accepted map, globally universal pure-input exactness and order, positive Pauli error sectors, a fixed pure nonfree target, and accepted stabilizer-cone preservation. It does not establish a 12-copy quadratic protocol, a physical gate-time lower bound, or optimality if uncharged magic catalysts or direction-dependent maps are added.
