# Scientific verification record

## Reproduced exact checks

On 29 October 2026 the two committed scientific scripts were copied from research revision `d17cdc9671b9fda37c1d313cf668e8a06ae88efc`, checked against their Git blob hashes, and executed again under Python 3.13.5 with NumPy 2.3.5. Both passed. The furnishing changes leave these scripts unchanged.

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
```

The first script uses exact integer NumPy arrays to construct the Kraus operators and tests syndrome maps, symmetric norms, code-size selection and buffering. The second builds every degree-six accepted error-label polynomial on the full mixed input and propagates all eight groups through a 64-state exact polynomial transfer map. It checks three small positive noise values as endpoints, not as a replacement for the analytical order argument.

## Scientific and learning review

The model, lower bound and construction were reviewed together for the fixed-map assumption, accepted free-state preservation, conditional error convention, global universality, promise-restricted success floor and charging of failed trials. The learning bridge keeps suppression order distinct from code distance and source noise distinct from faulty circuit locations. Its section pointers refer to the verified Gottesman arXiv v1, and the common map contains M01–M30 in a 12/18 phase allocation. Primary research ingredients remain separately attributed.

Markdown source was changed to GitHub's documented inline-math and fenced-math syntax. This source-level repair is not a claim of successful hosted rendering. The live GitHub page requests available during this review returned retrieval errors; actual hosted inspection of the README, bridge and representative proof pages remains pending.

## Evidence limits

The exact checks establish their instances and arithmetic. They do not reconstruct the imported algebraic-geometry decoder, prove the universal converse by enumeration, certify a practical factory, or constitute independent expert review. The literature comparison is retained from the research record; the anchor and the correcting-code source were rechecked during furnishing, while several previously inspected versioned 2026 full texts could not be fetched again. No exhaustive new priority search is claimed.
