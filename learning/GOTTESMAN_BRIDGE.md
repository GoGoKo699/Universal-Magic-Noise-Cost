# From Gottesman to universal magic noise cost

**Single anchor:** Daniel Gottesman, _An Introduction to Quantum Error Correction and Fault-Tolerant Quantum Computation_, [arXiv:0904.2557v1](https://arxiv.org/abs/0904.2557v1), 16 April 2009. [Author preprint PDF](https://arxiv.org/pdf/0904.2557v1).

A quantum processor needs non-Clifford resources as well as operations that protect against errors. This project asks what happens when the resource source is not calibrated: every raw qubit points in the same unknown pure direction before independent depolarizing noise is applied. The factory may inspect measurement outcomes, but its circuit cannot be chosen using that unknown direction or the unknown noise strength. On success it must emit one fixed CCZ state.

Gottesman is the educational entrypoint, not the source of the new copy-cost theorem. The distinctions and derivations below are supplied by this repository. Use the [milestone map](MILESTONES.md) to connect them to the complete [scientific account](../science/README.md).

## Source map

Section numbers are those in arXiv v1. Only the indicated concepts are needed initially; reading the whole chapter is not a prerequisite.

| Anchor sections | Foundation used here | Project destination |
|---|---|---|
| 2.1 | Pauli basis and error weight | [Noise model](../science/model.md), [positive fault sectors](../science/converse.md) |
| 2.2 | Detectable versus correctable error sets; code distance | Suppression order versus distance; [outer correction](../science/construction.md) |
| 2.3 | Stabilizer generators and syndromes | Six free rays; [finite detector](../science/finite_protocols.md) |
| 3.1 | CSS constructions and binary checks | The detector's binary matrices and inherited code ingredients |
| 3.4–3.5 | Logical Paulis and Clifford conjugation | Corrected accepted branches and free twirls |
| 4.5–4.6 | Gate teleportation and verified ancilla preparation | Fixed CCZ target, heralding and discarded inputs |
| 4.1 and 5 | Faulty circuit locations and threshold context | Why source-noise suppression is not a gate-noise threshold |

## Notation and resource translation

| Symbol or convention | Meaning in this project |
|---|---|
| $`n`$ | Maximum number of raw input qubits per run, including failures, not a code dimension |
| $`d`$ | Required order of conditional infidelity, not Gottesman's code-distance parameter |
| $`D_{\mathrm{code}}`$ | Code distance when distinguishing it from suppression order; correcting $`t`$ arbitrary errors ordinarily needs distance at least $`2t+1`$ |
| $`p`$ | Mixture weight in $`\rho_\psi(p)=(1-p)\psi+pI/2`$; nonidentity-Pauli probability in this representation is $`3p/4`$ |
| $`S_\psi(p)`$ | Probability that the entire factory accepts |
| $`e_\psi(p)`$ | Infidelity of the accepted output with the pure CCZ target |
| $`\eta(\psi)`$ | Infidelity to the nearest pure stabilizer ray, not the source-noise parameter |
| $`\eta_0,\alpha`$ | Public lower distance promise and required success floor, not unknown source parameters |

All states used to compute probabilities here are normalized. In particular, the anchor sometimes omits normalization when discussing codewords; that convention must not be transferred into acceptance probabilities. Stabilizer processing is ideal in this project. Gates, measurements, waiting and resets are not assigned a physical error model.

## B1. Accepted maps and the two probabilities

A successful outcome is represented before normalization by

```math
\Lambda(\omega)=\sum_j K_j\omega K_j^\dagger,
\qquad \sum_jK_j^\dagger K_j\le I.
```

The index includes every accepted outcome after its prescribed correction. Its trace is the probability of acceptance, not automatically one. Let $`\tau`$ be the pure CCZ target and define the unnormalized error probability

```math
H_\psi(p)=\mathrm{Tr}[(I-\tau)\Lambda(\rho_\psi(p)^{\otimes n})].
```

Then $`e_\psi(p)=H_\psi(p)/S_\psi(p)`$. Small $`H`$ alone need not imply an accurate accepted state when $`S`$ is small. The model requires positive ideal success for every nonstabilizer direction, so for each fixed direction division by $`S_\psi(p)`$ is regular sufficiently close to $`p=0`$. A uniform lower success floor is an additional requirement on directions satisfying the promise.

This is the measurement bookkeeping needed to connect Gottesman's syndrome and ancilla discussions to [model equations M3–M8](../science/model.md).

## B2. A complete six-copy example

Take the unknown-source example used in the exact verifier:

```math
|\psi\rangle=\frac{2|0\rangle+(1+i)|1\rangle}{\sqrt6},
\qquad (x,y,z)=(2/3,2/3,1/3).
```

Its nearest-stabilizer infidelity is $`\eta=(1-2/3)/2=1/6`$. The inherited concentrator measures $`X^{\otimes6}`$ and $`Z^{\otimes6}`$, keeps the specified minus-syndrome sector, then makes additional measurements and Clifford corrections. The [four full-space Kraus maps](../science/finite_protocols.md) specify every accepted branch. On ideal input, their total success is

```math
q_\psi(0)=\frac{1-x^6-y^6-z^6}{6}=\frac{100}{729},
\qquad \mathcal E_6(\psi^{\otimes6})=q_\psi(0)\tau.
```

A failure consumes its six inputs and returns no target. A success returns exactly CCZ at zero noise. Thus a single attempt has a charged budget of six, not six multiplied by its success probability.

For independently noisy copies the conditional concentration error begins as $`1107p/400+O(p^2)`$ for this direction. Combining eight such successes with the credited eight-CCZ detector eliminates all single faulty-resource labels. The resulting 48-raw-copy example has ideal success $`(100/729)^8`$ and retained-output error $`616167p^2/20000+O(p^3)`$. Both values are checked by [the exact verifier](../verification/check_full_48.py). Quadratic accuracy does not imply useful constant yield: this example accepts only about one run in eight million at zero noise.

The small example demonstrates the operations and error convention. The constant-yield upper bound instead buffers many independent attempts and uses a correcting code.

## B3. From Pauli errors to a rejection kernel

The qubit depolarizing mixture has a positive Pauli expansion:

```math
\rho_\psi(p)=(1-3p/4)\psi+
\frac p4(X\psi X+Y\psi Y+Z\psi Z).
```

On independent copies, a weight-$`r`$ Pauli pattern carries a nonnegative probability of order $`p^r`$. If the accepted output has error $`O_\psi(p^d)`$, every individual pattern of weight below $`d`$ must have zero accepted damage. Positive probabilities cannot cancel one another. This is stronger information than a small average at one nonzero noise value.

Zero damage says that the output of each accepted Kraus operator lies on the target line. The identity holds for every nonstabilizer direction. Continuity of each fixed-pattern expression extends it to a stabilizer direction. At such a direction, the low-weight Pauli input is itself a stabilizer state. An accepted stabilizer-preserving operation cannot turn it into a nonzero pure CCZ state. It must therefore reject it.

This is the project's additional bridge from error correction to resource geometry. Gottesman's Pauli and syndrome language supplies its prerequisites, but the all-direction continuation and rejection conclusion are proved in [the converse](../science/converse.md), not asserted as textbook results. The free-preservation requirement is on the accepted map; an unrestricted success branch cannot be made free merely by averaging it with failure.

## B4. Why the kernel limits success

Around the nearest stabilizer ray, write

```math
|\psi\rangle=\sqrt{1-\eta}|s\rangle+
 e^{i\phi}\sqrt\eta|s_\perp\rangle.
```

In $`n`$ identical copies, the squared norm of the component with exactly $`k`$ orthogonal excitations is $`\binom nk\eta^k(1-\eta)^{n-k}`$. The kernel removes all components with fewer than $`d`$ excitations. Applying the same argument at the antipodal stabilizer removes those with more than $`n-d`$. Trace nonincrease bounds acceptance by the surviving middle tail:

```math
S_\psi(0)\le\Pr\{d\le\mathrm{Bin}(n,\eta)\le n-d\}
\le\frac{n\eta}{d}.
```

The last inequality follows because a nonnegative integer random variable with mean $`n\eta`$ has probability at most $`n\eta/d`$ of being at least $`d`$. Thus a success floor $`\alpha`$ at distance $`\eta_0`$ forces $`n\ge\alpha d/\eta_0`$.

The algebraic argument complements this operational one. On a pure tensor input, every accepted amplitude is a degree-$`n`$ homogeneous polynomial in $`a,b`$. The kernel forces a zero of order at least $`d`$ at each of the six stabilizer rays. Hence it contains the factor $`[ab(a^4-b^4)]^d`$ and requires $`n\ge6d`$. Root multiplicity, the binomial projection and the distinction between a necessary effect and a physical free implementation are supplied by this repository.

## B5. How the construction matches the order

The six-copy success is comparable to $`\eta`$. Allocating $`O_\alpha(d/\eta_0)`$ raw copies therefore supplies $`O(d)`$ successful CCZ resources with constant probability. Selecting the first fixed number of successes from independent identical trials leaves their conditional states independent; the [buffer calculation](../verification/run_checks.py) checks a finite example, and [the construction](../science/construction.md) gives the general argument.

A free Clifford twirl removes coherence between CCZ error labels while preserving target fidelity. It does not make all seven nonzero labels equiprobable. An inherited deterministic correcting code handles any fewer than $`d`$ faulty resource inputs. The code-family spacing is explicitly accounted for so a linear-size choice exists for every integer $`d`$, not just a subsequence. This yields the matching $`O_\alpha(d/\eta_0)`$ budget.

The large existence constant and sufficient small-noise range are not engineering estimates. The code and concentration circuits remain attributed research dependencies. Neither the 48-copy example nor the algebraic lower bound establishes a 12-copy quadratic factory.

## B6. What the completed story does and does not say

The theorem combines a converse for all allowed accepted maps with a construction using ordinary stabilizer processing. It concerns exact ideal conversion and conditional infidelity under independent source depolarization. It does not give an optimal finite prefactor, a gate count, a runtime, a noisy-gate threshold or an approximate fixed-noise distillation theorem. Global universality remains required even outside the distance promise; only the uniform success floor is promise restricted.

The [30 milestones](MILESTONES.md) end by assembling these quantifiers and limitations with the proof, construction, attribution and reproduction evidence. Gottesman's discussion of faulty circuit locations is the appropriate contrast for understanding why the present source-noise result alone is not a physical fault-tolerance guarantee.
