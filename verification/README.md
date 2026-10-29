# Verification and limits

The analytical results are in [the converse](../science/converse.md) and [the construction](../science/construction.md). Finite computations check explicit matrix identities and resource arithmetic; they cannot certify a theorem for all pure directions, integers $`d`$, or external algebraic-geometry code genera.

Run from the repository root using Python 3.11 or later:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The two scripts use Python integers and `fractions.Fraction` for exact rational combinatorics, and NumPy arrays of `dtype=object` for the 64-dimensional full six-copy measurement. NumPy is pinned to version 2.3.5. No stochastic sampling, numerical optimization, network request, or quantum SDK is involved in the checks.

* [run_checks.py](run_checks.py): constructs and normalizes the four full-space concentration Kraus maps; checks 512 trilinear identity cases, all one- and two-error patterns of the eight-to-two code, the symmetric $`V_d`$ norms, a conservative all-order code-size bound and a conditional-buffer example.
* [check_full_48.py](check_full_48.py): on the generic pure qubit $`[2|0\rangle+(1+i)|1\rangle]/\sqrt6`$, builds the full iid noisy input and the degree-six polynomial for each of eight CCZ-error labels, then composes eight groups with the outer detector via a 64-state exact polynomial dynamic program. It checks the degree-48 acceptance polynomial and leading retained-output infidelity $`616167p^2/20000`$ against a separate weighted two-error pattern calculation. It also distinguishes the joint output coefficient $`1679859/40000`$.

The [verification report](../results/verification_report.md) records the concrete outputs and their limitations; the [finite-protocol account](../science/finite_protocols.md) defines the associated physical operations and noise convention.

The source-level decoder and code-existence theorem of Wills–Hsieh–Yamasaki remain inherited, not reconstructed by these checks. Likewise finite rank calculations and a sample 48-input state do not replace the universal analytical proofs. The [learning route](../learning/README.md) contains the selected Gottesman bridge and exactly 30 shared milestones. Source-level mathematical formatting checks are distinct from inspecting the actual GitHub renderer; see the review limits in the report.
