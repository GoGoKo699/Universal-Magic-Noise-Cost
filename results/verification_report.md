# Scientific verification record

## Reproduced exact checks

The scientific scripts passed on 29 October 2026 under Python 3.13.17 with NumPy 2.3.5 in GitHub Actions, and again under Python 3.13.5 with NumPy 2.3.5 in the local verification environment. The tested source was `f33a4a92128999f7942cb6e5233c434c209082cf`, in [verification run 40817613272](https://github.com/GoGoKo699/Universal-Magic-Noise-Cost/actions/runs/40817613272). Its scientific script blobs are unchanged from the original research integration.

| Check | Exact result | Meaning |
|---|---|---|
| Full concentration instrument | Four corrected 8-by-64 maps; accepted-effect rank eight | No substitution of a symmetric restriction on noisy inputs |
| Eight-CCZ detector | All 512 cubic identity cases pass | Ideal two-CCZ action |
| One resource-label fault | 56 cases; zero accepted | First-order error elimination |
| Two resource-label faults | 1372 total; 196 accepted | Second-order events |
| Error on either output | 184 accepted harmful patterns | Joint metric |
| Error on first output | 148 accepted harmful patterns | Retained metric |
| Symmetric root norm | $`V_1=1/3,V_2=8/231,V_3=2/663`$ | Algebraic normalization |
| Genus sequence | $`g_3=32705,\ B=67535825`$ | All-order rounding arithmetic |
| Conditional buffer | GG $`64/121`$; GB and BG $`24/121`$ each; BB $`9/121`$ | Conditional product distribution in the checked example |
| Full 48-copy polynomial | Degree 48; retained infidelity $`616167p^2/20000+O(p^3)`$ | Exact finite witness |
| Joint two-output error | Leading coefficient $`1679859/40000`$ | Distinct joint convention |

The example uses $`|\psi\rangle=[2|0\rangle+(1+i)|1\rangle]/\sqrt6`$. Ideal complete acceptance is $`(100/729)^8`$. The accepted six-copy output has leading conditional infidelity $`1107p/400`$. These rational values are asserted by the [full polynomial verifier](../verification/check_full_48.py).

The inspected script blobs are `55cabee3067327f4eb01bafbe2117e9eb3c15031` for `run_checks.py` and `760e4fe3e40e6b04e98c5394b4b8a6e0c3c6b97f` for `check_full_48.py`. This identifies the executed code independently of documentation-only commits.

## Reproduce

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
python verification/check_docs.py
python verification/check_math_contract.py
```

The scientific suite uses exact integer and rational arithmetic for the Kraus operators, syndrome maps, symmetric norms, code-size selection, buffering and the full degree-48 input polynomial. The document checker validates local links and the shared milestone map. The mathematical source checker rejects HTML-like inequality syntax and includes seven regression fixtures for missing relations, equation labels and math hosts.

For the separate live-host check, check out the exact commit to inspect, install `verification/hosted-requirements.txt` and Chromium, and run:

```bash
python -m pip install -r verification/hosted-requirements.txt
python -m playwright install chromium
python verification/check_hosted.py --revision "$(git rev-parse HEAD)"
```

The host check requires network access. It reads only this public repository's pages, compares full MathML text with the checked-out source, and retains screenshots, JSON evidence and a tracked-source ZIP in `hosted-check/`.

## Scientific and learning review

The model, lower bound and construction were reviewed together for the fixed-map assumption, accepted free-state preservation, conditional error convention, global universality, promise-restricted success floor and charging of failed trials. The learning bridge keeps suppression order distinct from code distance and source noise distinct from faulty circuit locations. Its section pointers refer to the verified Gottesman arXiv v1, and the common map contains M01–M30 in a 12/18 phase allocation. Primary research ingredients remain separately attributed.

The source checks passed for 14 Markdown pages, 153 local links, 30 correctly ordered milestones and 434 mathematical expressions at the tested revision. The seven regression fixtures passed both locally and in Actions.

## Hosted mathematics and visual inspection

The actual GitHub Chromium check passed for `README.md`, `learning/GOTTESMAN_BRIDGE.md`, `science/model.md`, `science/results.md`, `science/converse.md`, `science/construction.md` and `science/finite_protocols.md`. Across these seven pages, all 397 mathematical expressions rendered, their relation-symbol counts agreed with the source, and all 49 numbered equation labels were present. No renderer errors, zero-size formulas or page-wide horizontal overflow were reported at the checked 1440-pixel viewport.

The saved README, Gottesman bridge and converse screenshots were inspected visually. Separate detail screenshots confirm the complete strict-inequality conditions and labels in equations C1 and C6. Explicit `\lt` syntax also protects the construction's genus-bound inequalities. Checking that a math component exists is insufficient: the completeness regression checks also detect lost relations or missing equation labels.

The downloaded hosted-evidence ZIP from this run matched SHA256 `0ccb89e103cf92cc12eb0628958c8eae6c96c5f505879e8b5995f6639e29cd1d`. The run's retained artifact includes the exact public source used for those comparisons. Hosted artifact retention is finite; the commands above reproduce the checks. Mobile viewports and other browsers were not inspected.

## Evidence limits

The exact checks establish their instances and arithmetic. They do not reconstruct the imported algebraic-geometry decoder, prove the universal converse by enumeration, certify a practical factory, or constitute independent expert review. Relation and label checks are targeted display regressions, not a proof of mathematical equivalence for arbitrary rendered expressions. The literature comparison is retained from the research record; the anchor and the correcting-code source were rechecked during furnishing, while several previously inspected versioned 2026 full texts could not be fetched again. No exhaustive new priority search is claimed.
