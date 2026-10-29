# Scientific verification record

**Executed in the research runtime:** the integer/rational verification suite and the exact 48-copy polynomial calculation. The following assertions pass without stochastic simulation.

| Check | Exact result | Meaning |
|---|---|---|
| Full Rizzo–Leone accepted Kraus instrument | Four corrected 8-by-64 maps, accepted-effect rank eight | No erroneous substitution of symmetric restriction on noisy inputs |
| Eight-CCZ outer detector | All 512 cubic identity cases | Ideal two-CCZ action |
| One raw CCZ label fault | 56 labelled cases; zero accepted | First-order error elimination |
| Two raw CCZ label faults | 1372 total; 196 accepted | Necessary second-order scale |
| Error on either output | 184 accepted harmful patterns | Joint metric |
| Error on first output | 148 accepted harmful patterns | Actual retained metric |
| Symmetric root norm | \(V_1=1/3,V_2=8/231,V_3=2/663\) | Algebraic normalization |
| Genus sequence | \(g_3=32705,\;B=67535825\) | All-order rounding arithmetic |
| Buffer conditional distribution | Good/good \(64/121\), good/bad \(24/121\), bad/good \(24/121\), bad/bad \(9/121\) | Conditioning on success does not induce cross-trial error correlation |
| Full 48-copy input polynomial | Degree 48, leading one-output infidelity \(616167p^2/20000\) | Exact finite witness |
| Two-output error for same input | Leading coefficient \(1679859p^2/40000\) | Distinct joint convention |

The full polynomial calculation uses \(|\psi\rangle=[2|0\rangle+(1+i)|1\rangle]/\sqrt6\). The ideal complete acceptance probability is \((100/729)^8\). The accepted six-copy output has leading conditional infidelity \(1107p/400\). These rational values are asserted by the committed [full polynomial verifier](../verification/check_full_48.py).

### Reproduce

~~~bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
~~~

The first script constructs all six-copy Kraus operators with exact integer NumPy arrays, checks Pauli-projector normalization, the full outer-code syndrome map, symmetric norms, code-size selection and selected buffer conditioning. The second script computes every degree-six accepted CCZ label polynomial on the full mixed input and propagates all eight through a 64-state exact polynomial transfer map. Numerical evaluation of three small positive \(p\) values is an endpoint check, not an asymptotic proof.

These tests verify their explicit instances and exact algebraic arithmetic. They do **not** independently reconstruct the algebraic-geometry correcting code of Wills–Hsieh–Yamasaki, prove the entire all-direction converse (which is in [science/converse.md](../science/converse.md)), verify realistic hardware resources, or constitute independent referee certification.
