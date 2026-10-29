# Universal Magic Noise Cost

**How many copies of an unknown magic state are required to prepare a fixed CCZ state while suppressing independent input noise?**

The source is an unknown pure qubit direction, each copy independently depolarized. The factory is a *fixed* stabilizer protocol, exact on every pure nonstabilizer input at zero noise, and suppresses conditional output infidelity to order \(d\). Define its distance from the nearest pure stabilizer ray by

$$
\eta(\psi)=1-\max_{s\in\mathrm{Stab}_1}|\langle s|\psi\rangle|^2.
$$

Requiring ideal acceptance probability at least \(\alpha\in(0,1)\) for all directions with \(\eta(\psi)\ge\eta_0>0\) gives the optimal worst-case raw-copy budget

$$
\boxed{n_*(d,\eta_0;\alpha)=\Theta_\alpha(d/\eta_0).}
$$

This is an exact-input, fixed-map, ideal-stabilizer-processing result. Failed concentration attempts and discarded inputs count toward the copy budget. The public promise \(\eta_0\) controls only the *uniform success guarantee*; exact universality and order-\(d\) suppression apply to **every nonstabilizer pure input**.

| Result | Consequence | Source |
|---|---|---|
| Joint raw-copy law | Necessary and sufficient scaling \(d/\eta_0\) at fixed success \(\alpha\) | [Theorem and proof map](science/results.md) |
| Kernel converse | Every accepted Kraus operator annihilates fewer than \(d\) orthogonal flips around every stabilizer ray | [Converse](science/converse.md) |
| Finite yield envelope | \(S_\psi(0)\le\Pr\{d\le\mathrm{Bin}(n,\eta(\psi))\le n-d\}\) | [Converse](science/converse.md) |
| Algebraic obstruction | \(n\ge6d\), with multiplicity \(d\) at six stabilizer roots | [Converse](science/converse.md) |
| Explicit order-two example | 48 raw qubits: eight exact six-copy concentration attempts and an inherited eight-CCZ detector | [Finite protocol](science/finite_protocols.md) |

The **six-copy concentration circuit** and its ideal success formula are inherited from [Rizzo–Leone](references/RELATED_WORK.md#universal-pure-input-concentration); the outer correcting code is inherited from [Wills–Hsieh–Yamasaki](references/RELATED_WORK.md#constant-overhead-correction). The addition is the all-direction noise-to-kernel converse and its matching *joint* order/yield scaling.

## Science and verification

Start at the [scientific reading route](science/README.md), then the exact [model](science/model.md), [theorem](science/results.md), [converse](science/converse.md), [construction](science/construction.md), and [interpretation](science/interpretation.md). For the explicit small example see [finite protocols](science/finite_protocols.md). [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) identify imported mechanisms. [Verification](verification/README.md) and the [reader/LLM map](llms.txt) provide reproduction and navigation.

## Scope and limits

The input is \(\rho_\psi(p)=(1-p)|\psi\rangle\langle\psi|+pI/2\), independent across copies, with unknown \(\psi\) and \(p\). Accepted processing preserves stabilizer states. There is no free nonstabilizer catalyst or direction-dependent controller. The theorem is about the *maximum number of raw inputs per run*, not gate count, elapsed time, noisy processing, or an optimal fixed-noise threshold. The matching construction has large existence constants. The lower bound \(6d\) is **not** an achieved finite factory at every \(d\); a 12-copy quadratic factory has not been established.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
