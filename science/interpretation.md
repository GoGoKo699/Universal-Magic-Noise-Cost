# Interpretation: why robustness costs yield

Exact universal pure-state concentration and robust universal mixed-input conversion are distinct tasks. The ideal family $`|\psi\rangle^{\otimes n}`$ lies in the symmetric subspace, but $`\rho_\psi(p)^{\otimes n}`$ has contributions outside it. A rank-one symmetric restriction of an accepted measurement is not a valid replacement for its full physical action on independently noisy inputs.

The novel causal chain in [the converse](converse.md) is:

1. Conditional error order $`d`$ makes every Pauli pattern of weight below $`d`$ harmless; positivity forbids cancellations.
2. Global unknown-direction universality extends harmlessness to all six pure stabilizer rays.
3. A stabilizer-preserving accepted map cannot output a nonzero fixed nonstabilizer pure target when fed such a stabilizer input: it must reject the entire low-excitation subspace.
4. Near a free ray, the surviving amplitude of $`n`$ identical copies is a binomial tail controlled by their infidelity $`\eta`$ and required excitation order $`d`$.

Hence constant acceptance requires $`n\eta`$ to be of order $`d`$. The same kernel puts multiplicity $`d`$ at all six stabilizer roots and gives $`n\ge6d`$. These are joint statements about unknown-input direction, noise suppression, and success, not just a restatement of known-direction error correction or six-copy pure concentration.

[The upper construction](construction.md) shows this penalty can be met in raw-copy scaling. Each exact six-copy attempt succeeds with probability comparable to $`\eta`$; buffering on the order of $`d/\eta_0`$ copies accumulates on the order of $`d`$ CCZ resources with constant probability. An inherited correcting code suppresses the remaining noisy-output faults. No estimate of the unknown direction or extra nonstabilizer source is used.

The necessary algebraic shape at $`n=6d`$ does not show attainability. In fact the symmetric geometric effect at $`d=1`$ already permits a larger yield than ordinary stabilizer operations attain. Higher-order small-factory construction and sharp leading constants remain open.

This is an ideal stabilizer-operation and iid depolarization theorem with a fixed map and pure target. If the input is a correlated mixed source, the gate set is noisy, a catalyst supplies uncharged magic, or a protocol changes with the noise parameter, its resource boundary changes. Approximate asymptotic universal distillation under general resource-nongenerating maps is separately treated in [Lami–Regula–Takagi](../references/RELATED_WORK.md#other-comparisons) and does not imply finite-block exact robustness as defined here.
