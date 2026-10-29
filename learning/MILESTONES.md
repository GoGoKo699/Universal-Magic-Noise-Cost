# Thirty milestones for understanding universal magic noise cost

The single anchor is [Gottesman, arXiv:0904.2557v1](https://arxiv.org/abs/0904.2557v1), abbreviated **G**. Section references refer to that version. **B1–B6** refer to the [project bridge](GOTTESMAN_BRIDGE.md). The authoritative results remain under [science/](../science/README.md).

This common map has 12 background/preliminaries milestones and 18 narrative/innovation milestones. Each phase moves from individual objects to their combined operational meaning. Prerequisites, dependencies and targets are defined by the project, not by an individual reader's progress. The map aims at global understanding, not coverage of every specialist detail.

## Phase I: Background and preliminaries

### M01. What is the unknown source?
**Question:** What remains fixed and what remains unknown across raw copies?

**Understanding target:** Explain a normalized pure qubit, its density operator and identical independent preparations without treating its amplitudes as supplied classical data.

**Dependencies and connection:** None. Establishes the physical input before introducing errors or allowed processing.

**Sources:** G §1; [model M1](../science/model.md); [B2](GOTTESMAN_BRIDGE.md#b2-a-complete-six-copy-example).

### M02. How does independent depolarization change the input?
**Question:** What does the mixture parameter describe?

**Understanding target:** Distinguish the ideal state, the maximally mixed replacement and the equivalent nonidentity-Pauli probability of three quarters of the mixture weight.

**Dependencies and connection:** M01. Connects the raw source to a positive tensor-product fault model rather than a common coherent rotation.

**Sources:** G §2.1; [model M1](../science/model.md); [B3](GOTTESMAN_BRIDGE.md#b3-from-pauli-errors-to-a-rejection-kernel).

### M03. Why use Pauli patterns and their weight?
**Question:** What does a low-weight pattern count?

**Understanding target:** Describe tensor products of identity and Pauli operators, their support size and the probability order of a fixed pattern under independent depolarization.

**Dependencies and connection:** M02. Makes the later low-fault argument an assertion about specific input locations.

**Sources:** G §2.1; [converse C5](../science/converse.md).

### M04. Which qubit directions are free?
**Question:** Why are there six pure stabilizer rays?

**Understanding target:** Identify the two eigenstates of each Pauli axis and distinguish a pure stabilizer ray from a convex mixture of stabilizer states.

**Dependencies and connection:** M01, M03. Introduces the resource boundary that will force rejection rather than successful conversion.

**Sources:** G §2.3; [model M4 and M7](../science/model.md).

### M05. What do Clifford gates and stabilizer measurements preserve?
**Question:** Which processing resources are allowed without supplying extra magic?

**Understanding target:** Explain Clifford conjugation, stabilizer ancillas, Pauli measurements and classical feedforward, including why postselection is still constrained on free inputs.

**Dependencies and connection:** M03, M04. Connects the circuit language to accepted stabilizer-cone preservation.

**Sources:** G §§3.4–3.5; [model M3–M4](../science/model.md); [B1](GOTTESMAN_BRIDGE.md#b1-accepted-maps-and-the-two-probabilities).

### M06. Why choose a fixed CCZ output?
**Question:** How does a prepared state supply a non-Clifford operation?

**Understanding target:** Describe the CCZ target and the role of a resource state in gate injection without counting an already available non-Clifford gate as free.

**Dependencies and connection:** M05. Relates the output requirement to quantum computation rather than abstract state purification.

**Sources:** G §4.5; [model M2](../science/model.md); [construction §2](../science/construction.md).

### M07. What information does an accepted map retain?
**Question:** How can many corrected success branches be described together?

**Understanding target:** Explain an unnormalized completely positive output, its acceptance effect and the trace-nonincreasing constraint.

**Dependencies and connection:** M05, M06. Supplies the mathematical description used by both converse and construction.

**Sources:** G §§2.3 and 4.6 as measurement context; [B1](GOTTESMAN_BRIDGE.md#b1-accepted-maps-and-the-two-probabilities); [model M3](../science/model.md).

### M08. How do accuracy and acceptance differ?
**Question:** Why must output error be conditioned on success?

**Understanding target:** Relate accepted infidelity to unnormalized damage divided by acceptance probability; distinguish either from unconditional success-and-correctness probability.

**Dependencies and connection:** M07. Prevents postselection from hiding a bad output behind a small success probability.

**Sources:** [B1](GOTTESMAN_BRIDGE.md#b1-accepted-maps-and-the-two-probabilities); [model M5](../science/model.md).

### M09. What does suppression order mean?
**Question:** Is order two the same as distance two?

**Understanding target:** Interpret pointwise conditional error of order at least d, and distinguish it from code distance, decoding radius and a fixed finite-noise error target.

**Dependencies and connection:** M03, M08. Connects the project's objective to coding language without conflating its parameters.

**Sources:** G §2.2; [notation table](GOTTESMAN_BRIDGE.md#notation-and-resource-translation); [model M6](../science/model.md).

### M10. How close is a source to a stabilizer ray?
**Question:** Which geometry controls the weak-resource limit?

**Understanding target:** Interpret nearest-ray infidelity through the largest absolute Bloch coordinate and recognize its maximum possible value.

**Dependencies and connection:** M01, M04. Supplies the distance parameter that will enter the copy-cost law independently of noise.

**Sources:** [model M7](../science/model.md); [B2](GOTTESMAN_BRIDGE.md#b2-a-complete-six-copy-example).

### M11. What counts as the cost of a run?
**Question:** Are failed concentration attempts free?

**Understanding target:** Count the maximum raw inputs including failed and discarded trials, and distinguish this budget from expected repetitions, output yield and physical hardware cost.

**Dependencies and connection:** M07, M08. Fixes the resource comparison before comparing lower and upper bounds.

**Sources:** G §§4.6 and 5 as contrast; [model](../science/model.md); [B2](GOTTESMAN_BRIDGE.md#b2-a-complete-six-copy-example).

### M12. What is the full universal-factory contract?
**Question:** Which requirements hold everywhere and which are promise restricted?

**Understanding target:** Assemble fixed-map processing, exact ideal CCZ output, positive ideal acceptance and pointwise noise order on every nonstabilizer ray, with a uniform success floor only above the public distance promise.

**Dependencies and connection:** M01–M11. Integrates the foundations into the precise optimization task.

**Sources:** [model M1–M8](../science/model.md); [results T1](../science/results.md); [B6](GOTTESMAN_BRIDGE.md#b6-what-the-completed-story-does-and-does-not-say).

## Phase II: Narrative and innovation

### M13. What does the known six-copy concentrator already supply?
**Question:** Why is exact pure-input concentration not the new theorem?

**Understanding target:** Explain the inherited ideal conversion, success formula and degree-six stabilizer-root polynomial, with attribution separated from the new noisy-input claim.

**Dependencies and connection:** M06, M10, M12. Establishes the starting capability and the remaining question.

**Sources:** [related work](../references/RELATED_WORK.md#universal-pure-input-concentration); [construction U1](../science/construction.md); [B2](GOTTESMAN_BRIDGE.md#b2-a-complete-six-copy-example).

### M14. Why can low-order damage not cancel?
**Question:** What does positivity add to an error expansion?

**Understanding target:** Infer zero accepted damage for every pattern below the requested order from the nonnegative pattern sum, rather than from cancellation of a formal Taylor series.

**Dependencies and connection:** M03, M08, M09, M12. Gives the first load-bearing step of the converse.

**Sources:** [converse, positive fault sectors](../science/converse.md#proof-positive-fault-sectors); [B3](GOTTESMAN_BRIDGE.md#b3-from-pauli-errors-to-a-rejection-kernel).

### M15. How does universality reach a free input?
**Question:** Can the limiting argument work without a uniform error constant?

**Understanding target:** Explain continuity of each zero-damage fixed-pattern expression at a stabilizer ray and why this does not require exchanging a nonuniform asymptotic bound with a limit.

**Dependencies and connection:** M12, M14. Uses unknown-direction universality to strengthen a familiar harmless-pattern argument.

**Sources:** [converse C5–C6](../science/converse.md); [B3](GOTTESMAN_BRIDGE.md#b3-from-pauli-errors-to-a-rejection-kernel).

### M16. Why must a harmless free input be rejected?
**Question:** What turns zero damage into zero acceptance?

**Understanding target:** Combine purity of the required nonstabilizer target, accepted free-state preservation and positivity to conclude that every accepted Kraus operator annihilates the input.

**Dependencies and connection:** M04–M08, M15. Identifies the consequential new connection between noise robustness and resource restrictions.

**Sources:** [converse C6](../science/converse.md); [model M4](../science/model.md); [B3](GOTTESMAN_BRIDGE.md#b3-from-pauli-errors-to-a-rejection-kernel).

### M17. What is the full rejected subspace?
**Question:** Why is a symmetric pure-state restriction insufficient for noise analysis?

**Understanding target:** Describe all product strings with fewer than d orthogonal flips around every stabilizer ray and the resulting full input-space kernel.

**Dependencies and connection:** M03, M16. Extends the argument from individual faults to the acceptance-effect constraint.

**Sources:** [converse C1–C2](../science/converse.md); [finite protocol F1–F3](../science/finite_protocols.md).

### M18. How does projection produce a binomial envelope?
**Question:** What fraction of ideal input norm survives the kernel?

**Understanding target:** Expand identical copies around a nearest stabilizer, recognize the binomial weights, and explain rejection of both low and high excitation sectors.

**Dependencies and connection:** M10, M17. Converts a linear-algebraic kernel into an operational bound on success.

**Sources:** [converse C3–C4](../science/converse.md); [B4](GOTTESMAN_BRIDGE.md#b4-why-the-kernel-limits-success).

### M19. Why do distance and suppression order multiply in the cost?
**Question:** Why is a separate bound in each parameter insufficient?

**Understanding target:** Combine the success floor with the binomial mean bound to obtain the lower cost proportional to d divided by the distance promise.

**Dependencies and connection:** M11, M12, M18. Extracts the joint lower law rather than only a finite-block obstruction.

**Sources:** [converse C7](../science/converse.md); [results T1](../science/results.md); [B4](GOTTESMAN_BRIDGE.md#b4-why-the-kernel-limits-success).

### M20. Why does each stabilizer root have multiplicity d?
**Question:** How does a rejected excitation sector constrain an amplitude polynomial?

**Understanding target:** Relate derivatives along a projective coordinate to low-excitation terms and infer divisibility by the d-th power of the sextic, giving the lower bound of 6d copies.

**Dependencies and connection:** M13, M17. Connects the operational kernel to the algebraic necessary condition without claiming a construction.

**Sources:** [converse T3](../science/converse.md#t3-six-root-multiplicity); [B4](GOTTESMAN_BRIDGE.md#b4-why-the-kernel-limits-success).

### M21. Why is a geometric ceiling not a physical protocol?
**Question:** Does a one-dimensional surviving space establish attainability?

**Understanding target:** Interpret the symmetric-space dimension and projection envelope, using the six-copy case to distinguish a necessary positive effect from an attainable free operation.

**Dependencies and connection:** M17, M20. Delimits the claim at the algebraic minimum and preserves the open finite-block problem.

**Sources:** [converse T4](../science/converse.md#t4-symmetric-projection-envelope); [interpretation](../science/interpretation.md).

### M22. What errors emerge from noisy concentration?
**Question:** Must the conditional accepted state still be depolarized?

**Understanding target:** Use the all-ideal tensor contribution to bound success and conditional error without assuming isotropic output noise.

**Dependencies and connection:** M02, M08, M13. Starts achievability with a rigorously controlled noisy inner primitive.

**Sources:** [construction U2–U4](../science/construction.md); [finite protocol F11–F12](../science/finite_protocols.md).

### M23. Why is the CCZ error-basis twirl free?
**Question:** Does writing CCZ inside a conjugation charge another magic resource?

**Understanding target:** Explain direct Clifford conjugated-shift implementations and why twirling removes coherence but does not equalize nonzero error-label probabilities.

**Dependencies and connection:** M05, M06, M22. Makes the outer-code input convention physically admissible.

**Sources:** G §§3.5 and 4.5; [construction U5](../science/construction.md); [B5](GOTTESMAN_BRIDGE.md#b5-how-the-construction-matches-the-order).

### M24. How is an outer code selected for every order?
**Question:** Why does an asymptotically good family alone not settle every integer d?

**Understanding target:** Account for conversion groups, decoder radius and bounded gaps between allowed code sizes, while identifying the inherited coding theorem.

**Dependencies and connection:** M09, M23. Establishes linear outer-resource count with the exact quantifier used by the headline theorem.

**Sources:** G §3.1 as coding context; [construction U6–U7](../science/construction.md); [code attribution](../references/RELATED_WORK.md#constant-overhead-correction).

### M25. Does selecting the first successes correlate their errors?
**Question:** What happens after conditioning on enough successful trials?

**Understanding target:** Explain the tensor-product state conditional on a complete binary flag pattern and why mixing such patterns preserves the retained conditional product state.

**Dependencies and connection:** M07, M08, M22. Justifies the input independence used by the outer decoder.

**Sources:** [construction §4](../science/construction.md); [buffer verifier](../verification/run_checks.py); [B5](GOTTESMAN_BRIDGE.md#b5-how-the-construction-matches-the-order).

### M26. How does buffering give constant success at the claimed cost?
**Question:** Why do failed inner trials not change the scaling exponent?

**Understanding target:** Relate the number of allocated trials to their success mean, use a binomial lower-tail guarantee, and count all six raw inputs per attempt.

**Dependencies and connection:** M11, M24, M25. Produces the matching raw-copy upper bound at fixed success floor.

**Sources:** [construction U8–U11](../science/construction.md); [results T1–T2](../science/results.md).

### M27. What exactly does the 48-copy example establish?
**Question:** How can a low-yield finite factory still be a useful witness?

**Understanding target:** Follow eight full six-copy instruments into the inherited detector and distinguish single-output error from joint two-output error and from uniform success.

**Dependencies and connection:** M08, M13, M22, M23. Grounds the general reasoning in a completely specified finite construction.

**Sources:** G §§2.3 and 4.6 as syndrome context; [finite protocols](../science/finite_protocols.md); [B2](GOTTESMAN_BRIDGE.md#b2-a-complete-six-copy-example).

### M28. What does reproduction verify?
**Question:** Which conclusions follow from the exact scripts and which require proof?

**Understanding target:** Interpret the matrix-rank, syndrome-count, rational polynomial, conditioning and code-rounding checks without promoting finite tests to universal theorems or an independent decoder reconstruction.

**Dependencies and connection:** M21, M24–M27. Connects evidence to its exact claim and resource scope.

**Sources:** [verification guide](../verification/README.md); [verification report](../results/verification_report.md); [converse](../science/converse.md).

### M29. What is added beyond the closest prior work?
**Question:** Which part remains after crediting concentration and error correction?

**Understanding target:** Separate the inherited sextic, concentrator, harmless-fault method and correcting codes from the all-direction rejection kernel and the matched joint order/yield law; distinguish the internal catalytic-memory task.

**Dependencies and connection:** M13–M28. Integrates the novelty comparison at the level of actual models and consequences.

**Sources:** [related work](../references/RELATED_WORK.md); [interpretation](../science/interpretation.md); [B6](GOTTESMAN_BRIDGE.md#b6-what-the-completed-story-does-and-does-not-say).

### M30. What is the complete result, including its limits?
**Question:** What may be concluded about an unknown-source magic factory?

**Understanding target:** Present the matching raw-copy law, its accepted-map converse and ordinary-stabilizer construction, with global exactness, source-noise, distance-promise and success quantifiers intact. Explain why it proves neither an optimal finite prefactor nor a physical noisy-gate threshold.

**Dependencies and connection:** M12, M19–M29. Synthesizes the whole scientific story and its unresolved finite-block boundary.

**Sources:** [results](../science/results.md); [model](../science/model.md); [interpretation](../science/interpretation.md); G §§4.1 and 5 as contrast; [B6](GOTTESMAN_BRIDGE.md#b6-what-the-completed-story-does-and-does-not-say).
