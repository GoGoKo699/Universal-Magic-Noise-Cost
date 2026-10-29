# Model and operational contract

## Input, target and noise

Write an unknown normalized pure qubit as $`|\psi\rangle=a|0\rangle+b|1\rangle`$, with $`|a|^2+|b|^2=1`$, and put $`\psi=|\psi\rangle\langle\psi|`$. Its $`n`$ independently depolarized copies are

```math
\rho_\psi(p)^{\otimes n},\qquad
\rho_\psi(p)=(1-p)\psi+\tfrac p2 I_2,\quad 0\le p\le1.
\tag{M1}
```

Equivalently $`\rho_\psi(p)=(1-3p/4)\psi+(p/4)(X\psi X+Y\psi Y+Z\psi Z)`$. Thus $`p`$ is the depolarizing mixture weight, not the probability $`3p/4`$ of a nonidentity Pauli in this representation.

The fixed three-qubit target is

```math
|\mathrm{CCZ}\rangle=2^{-3/2}\sum_{u\in\{0,1\}^3}(-1)^{u_1u_2u_3}|u\rangle,\quad
\tau=|\mathrm{CCZ}\rangle\langle\mathrm{CCZ}|.
\tag{M2}
```

It is a pure nonstabilizer state. The resource is $`n`$, the maximum number of raw input qubits used per run. Rejected and discarded input copies are charged, including unused copies in a fixed input allocation.

## Operations and acceptance

A stabilizer factory may add free stabilizer ancillas, apply Clifford unitaries, perform Pauli measurements, use classical randomness and feedforward, discard and postselect. All nonstabilizer states consumed, including a possible catalyst, must be charged; this project supplies no catalyst. Stabilizer processing and storage are ideal.

Combining all accepted branches after their corrections yields a completely positive, trace-nonincreasing map

```math
\Lambda:\mathcal L((\mathbb C^2)^{\otimes n})\to\mathcal L((\mathbb C^2)^{\otimes3}).
\tag{M3}
```

The map is fixed independently of the unknown $`\psi`$ and unknown noise $`p`$, but can depend on the public design parameters $`d,\eta_0,\alpha`$. Adaptation to observed measurement outcomes is allowed.

The converse uses only accepted stabilizer-cone preservation:

```math
\Lambda(\mathrm{cone}(\mathrm{STAB}_n))\subseteq\mathrm{cone}(\mathrm{STAB}_3).
\tag{M4}
```

Here $`\mathrm{STAB}_r`$ is the convex hull of pure $`r`$-qubit stabilizer states and $`\mathrm{cone}`$ permits nonnegative scalar multiples. This includes ordinary stabilizer factories, and does not require each Kraus operator in an arbitrary decomposition of $`\Lambda`$ to be individually free. A larger operation being free only after successes and failures are averaged is not sufficient.

## Exactness and suppression order

Define acceptance and conditional pure-target infidelity:

```math
S_\psi(p)=\operatorname{Tr}\Lambda(\rho_\psi(p)^{\otimes n}),\qquad
e_\psi(p)=\frac{\operatorname{Tr}[(I-\tau)\Lambda(\rho_\psi(p)^{\otimes n})]}{S_\psi(p)}.
\tag{M5}
```

For every nonstabilizer pure input direction we require

```math
S_\psi(0)>0,\quad
\Lambda(\psi^{\otimes n})=S_\psi(0)\tau,\quad
e_\psi(p)=O_\psi(p^d)\quad(p\downarrow0).
\tag{M6}
```

The implicit noise constant can depend on $`\psi`$. Suppression order at least $`d`$ allows greater order. Exactness is at the single fixed zero-noise input, not an approximate pure-input statement. For small enough $`p>0`$, $`S_\psi(p)>0`$ follows from continuity.

## Distance and uniform yield

The six pure one-qubit stabilizer rays are the eigenstates of $`X,Y,Z`$. Define

```math
\eta(\psi)=1-\max_{s\in\mathrm{Stab}_1}|\langle s|\psi\rangle|^2
=\frac{1-\max\{|x|,|y|,|z|\}}2,\quad x^2+y^2+z^2=1.
\tag{M7}
```

Thus $`0\le\eta\le\eta_{\max}=(1-1/\sqrt3)/2`$. Every value in this interval is realized by a pure direction, for example the Bloch family $`(x,y,z)=(\sin\theta/\sqrt2,\sin\theta/\sqrt2,\cos\theta)`$ for $`0\le\theta\le\arccos(1/\sqrt3)`$.

For fixed $`d\ge1`$, $`\alpha\in(0,1)`$, and $`0<\eta_0\le\eta_{\max}`$, require

```math
\inf_{\psi:\eta(\psi)\ge\eta_0}S_\psi(0)\ge\alpha.
\tag{M8}
```

Only this floor is restricted by the distance promise. Conditions (M6) still apply to every nonstabilizer ray, including those with $`\eta<\eta_0`$; this is vital even when $`\eta_0=\eta_{\max}`$.

Define $`n_*(d,\eta_0;\alpha)`$ as the minimum maximum-input count over ordinary stabilizer factories satisfying (M6) and (M8). The converse holds for the larger class (M4).

## Six-root invariant

The inherited concentration polynomial for a pure qubit is

```math
f_6(a,b)=ab(a^4-b^4),\qquad
M_3^{\mathrm{lin}}(\psi)=6|f_6(a,b)|^2
=\frac{1-x^6-y^6-z^6}{2}.
\tag{M9}
```

Its six projective roots are exactly the stabilizer directions. The construction uses the inherited six-copy success $`q_\psi(0)=M_3^{\mathrm{lin}}/3`$. [The converse](converse.md) shows why robust order $`d`$ forces multiplicity $`d`$ at each root.

## Not covered

The result does not include correlated or coherent input noise, uncharged magic ancillary states, noisy Clifford operations, physical runtime, gate count, or a protocol changed with $`p`$. Trace distance is not substituted for the defined conditional infidelity.
