# T1: Joint raw-copy cost of universal magic noise suppression

Fix any $`\alpha\in(0,1)`$. For any integer $`d\ge1`$ and $`0<\eta_0\le\eta_{\max}:=(1-1/\sqrt3)/2`$, let $`n_*(d,\eta_0;\alpha)`$ be the minimum raw-copy budget in the [model](model.md).

**Theorem T1.** There is a constant $`C_\alpha<\infty`$, independent of $`d,\eta_0`$, such that

```math
\boxed{\max\{6d,\alpha d/\eta_0\}\le n_*(d,\eta_0;\alpha)\le C_\alpha d/\eta_0.}
\qquad\text{(T1)}
```

Therefore $`n_*(d,\eta_0;\alpha)=\Theta_\alpha(d/\eta_0)`$. The upper protocol is fixed independently of the unknown direction and noise, exact on all ideal pure nonstabilizer inputs, and has conditional output infidelity of order at least $`d`$ on every such input.

More concretely, the upper construction supplies positive constants $`b_\alpha,c_\alpha`$ independent of $`d,\eta_0,\psi`$ such that, uniformly for $`\eta(\psi)\ge\eta_0`$ and $`0\le p\le c_\alpha\eta_0`$,

```math
S_\psi(p)\ge\alpha,\qquad
e_\psi(p)\le(b_\alpha p/\eta_0)^d.
\qquad\text{(T2)}
```

These are sufficient existence constants, not an optimized fault-tolerant factory threshold.

## Why the lower bound holds

[Converse T2](converse.md) proves that every Kraus operator of any accepted stabilizer-preserving map kills all product strings with fewer than $`d`$ orthogonal flips around each free stabilizer ray. Expanding ideal input copies around a nearest ray gives

```math
S_\psi(0)\le\Pr\{d\le\mathrm{Bin}(n,\eta(\psi))\le n-d\}
\le\frac{n\,\eta(\psi)}d.
\qquad\text{(T3)}
```

A direction with $`\eta(\psi)=\eta_0`$ exists; the success floor forces $`n\ge\alpha d/\eta_0`$. [Converse T3](converse.md#t3-six-root-multiplicity) shows that the ideal accepted amplitude has a root of order $`d`$ at each of the six stabilizer rays, hence is divisible by $`f_6(a,b)^d`$ and necessarily has degree $`n\ge6d`$.

Neither lower bound assumes a specific stabilizer code, a single measurement round, or a particular Kraus decomposition.

## Why the upper bound holds

The [construction](construction.md) uses two credited primitives:

* The Rizzo–Leone six-copy universal exact concentrator, with ideal success $`q_\psi(0)=(1-x^6-y^6-z^6)/6`$, obeying $`\eta(\psi)/3\le q_\psi(0)\le2\eta(\psi)`$.
* The Wills–Hsieh–Yamasaki deterministic correcting CCZ distillation code family, which can be instantiated with $`m_d\le Bd`$ CCZ inputs and exact correction of any fewer than $`d`$ faulty input resources. The explicit bounded-ratio genus sequence verifies the quantifier for every integer $`d`$; the code and conversion methods are inherited.

Run $`L=\lceil(12m_d+48\ln(1/(1-\alpha)))/\eta_0\rceil`$ independent six-copy attempts. If fewer than $`m_d`$ succeed, report failure; otherwise pass the first $`m_d`$ successes to the correcting code. Conditioning on successful flags preserves independence of the retained accepted outputs. Both failed and successful trials count: $`n=6L=O_\alpha(d/\eta_0)`$. The proof of the finite-noise estimate (T2) is in [construction.md](construction.md).

## Stronger finite statements

The bound (T3) is a binomial middle-tail envelope for every $`n,d,\psi`$, not only an asymptotic statement. Also $`S_\psi(0)\le\binom nd\eta(\psi)^d`$: at fixed block size, yield vanishes with at least the $`d`$-th power of the stabilizer distance. The [converse](converse.md) derives the symmetric projection envelope with dimension $`\max\{n-6d+1,0\}`$. At $`n=6d`$, ideal success is proportional to $`[M_3^{\mathrm{lin}}(\psi)]^d`$ if such a factory exists.

A concrete 48-input order-two factory is specified in [finite protocols](finite_protocols.md). Its low ideal yield is not a contradiction: constant yield requires a budget proportional to $`d/\eta_0`$.

## Scientific boundary

This is a matching raw-copy scaling, not a proof that $`6d`$ inputs suffice, that leading constants are sharp, or that the inherited code has practical implementation costs. Exact ideal input, fixed map, independent depolarization, pure fixed target, and charged nonstabilizer supplies are load-bearing hypotheses. General asymptotic approximate resource-distillation rates concern another contract. The [related-work review](../references/RELATED_WORK.md) makes that distinction explicit.
