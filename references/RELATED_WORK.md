# Primary sources and contribution boundaries

This project concerns a *fixed* accepted stabilizer operation on unknown pure qubit input directions, exact ideal CCZ output, and independent depolarizing input-noise suppression of prescribed order. Success is uniformly bounded only under a public nearest-stabilizer-distance promise. Its new statement is the joint lower and upper raw-copy cost \(n_*(d,\eta_0;\alpha)=\Theta_\alpha(d/\eta_0)\), not a new six-copy concentrator or error-correcting code.

## Universal pure-input concentration

**Jacopo Rizzo and Lorenzo Leone, _Universal magic state concentration_, arXiv:2608.13376v2 (30 September 2026).** [Versioned text](https://arxiv.org/html/2608.13376v2).

Lemma 3 identifies the homogeneous ideal vanishing on the six pure-qubit stabilizer rays. Theorem 5 and Appendix B.1 give the six-copy exact concentration circuit and its accepted full-space instrument (Eqs. 67–77); Eq. 39 gives conversion to CCZ. Appendix C.1 gives the concentration yield \(M_3^{\rm lin}/3\). **Inherited:** ideal six-copy threshold, degree-six sextic, Clifford conversion, and ideal success. **Added here:** order-\(d\) *multiplicity* and the full low-error product-space kernel under independent noise, and a consequent binomial bound on yield.

## Harmless-error positivity

**Llorenç Balada Gaggioli and Jakub Mareček, _The limits of magic-state distillation_, arXiv:2610.31115v1 (22 October 2026).** [Versioned text](https://arxiv.org/html/2610.31115v1).

Section II formulates harmless low-weight error patterns for calibrated noisy T inputs. Positive fault sectors cannot cancel one another. **Inherited:** the harmless-pattern idea and its known-input source framework. **Added here:** extension to *every unknown input direction* and then to all six stabilizer rays, where resource preservation forces outright rejection; the resulting full Kraus kernel and uniform copy/yield law are not a specialization of the known-T setting.

## Constant-overhead correction

**Adam Wills, Min-Hsiu Hsieh and Hayata Yamasaki, _Constant-overhead magic state distillation_, Nature Physics 21, 1842–1846 (2025), DOI 10.1038/s41567-025-03026-0.** [Publisher](https://doi.org/10.1038/s41567-025-03026-0); [proof preprint, arXiv:2408.07764v2](https://arxiv.org/html/2408.07764v2).

Sections 4.2 and 4.4, Example 5.3.1, §6, and Appendix B give free twirling, the CCZ/qudit resource conversions, a correcting code over \(\mathbb F_{1024}\), and a decoder without heralded failure. The construction here uses **70 CCZ inputs per qudit** in one explicit decomposition. The code's genus sequence has bounded consecutive ratios and radius \(\lfloor g/8\rfloor\), which permits an explicit bound at *every integer* target error-suppression order. **Inherited:** code, conversions, decoder, constant-overhead distillation. **Added:** buffering unknown-direction concentration with raw input accounting and jointly matching universal yield-distance and noise-order scaling. The separate catalytic conversion to T resources is not invoked.

## The eight-CCZ detector

**Christopher Chamberland et al., _Building a Fault-Tolerant Quantum Computer Using Concatenated Cat Codes_, PRX Quantum 3, 010329 (2022), DOI 10.1103/PRXQuantum.3.010329.** [Published manuscript](https://preskill.caltech.edu/pubs/preskill-2022-building.pdf).

Appendix O, Eqs. O24–O26, Fig. 60, Algorithm 2, and Eqs. O39–O73 provide an eight-CCZ-to-two-CCZ error detector with its Clifford corrections and error map. This is the **inherited detector** used after eight six-copy concentration attempts in the explicit 48-raw-copy example. Exact composition with a noisy unknown-input full instrument distinguishes single retained CCZ error from joint two-CCZ error. The detector itself is not claimed new.

## Other comparisons

**Quynh T. Nguyen, _Good binary quantum codes with transversal CCZ gate_, arXiv:2408.10140v2.** [Text](https://arxiv.org/html/2408.10140v2). Asymptotically good binary CSS codes with transversal CCZ give another potential outer ingredient, but this source does not by itself supply the decoding and bounded-size-gap facts needed for the all-\(d\) upper theorem.

**Amolak Ratan Kalra and Shiroman Prakash, _Invariant Theory, Magic State Distillation, and Bounds on Classical Codes_, arXiv:2501.10163v3.** [Text](https://arxiv.org/html/2501.10163v3). Invariant/weight-enumerator constraints for specified codes and directions do not directly imply an arbitrary accepted-map kernel for all unknown directions.

**Simon Burton and Hussain Anwar, _Meromorphic Quantum Computing_, arXiv:2605.06251v1.** [Text](https://arxiv.org/html/2605.06251v1). Their constraints concern nonconstant coherent projective-state maps, while here the ideal successful output ray is constant and common amplitude factors determine yield.

**Ludovico Lami, Bartosz Regula and Ryuji Takagi, _Universal quantum resource distillation via composite generalised quantum Stein's lemma_, arXiv:2605.15174v1.** [Text](https://arxiv.org/html/2605.15174v1). Asymptotically approximate universal distillation under its resource-nongeneration classes is not finite exact-at-zero-noise conversion with a fixed noise-suppression order.

**Internal cross-project comparison.** [Catalytic-Magic-Memory](https://github.com/GoGoKo699/Catalytic-Magic-Memory) analyzes exact-return stored magic and stream error floors (inspected commit 2d6575c2aea964a9a521bce65eb72ea2a61181ec). Its fresh input is *specified*, its persistent catalyst is a charged separate resource, and its objective is indefinite output reuse, not unknown-direction finite exact noise-order suppression. [Universal-Entanglement-Readout](https://github.com/GoGoKo699/Universal-Entanglement-Readout) studies fixed-copy universal entanglement classification (inspected commit ca3bef037a20054319e2760a3a9be1f887a9589f), with a different object, target, and measurement model. Shared polynomial-rigidity tools do not imply this factory's new kernel.

## Attribution boundary

The scientific source [results](../science/results.md), [converse](../science/converse.md) and [construction](../science/construction.md) make the new statement precise; inherited operations are fully identified there. The comparisons are source-level checks of the most threatening nearby results, not exhaustive priority certification or independent expert referee reports. Leading constants, a minimal quadratic block, and noisy-processing costs remain open.
