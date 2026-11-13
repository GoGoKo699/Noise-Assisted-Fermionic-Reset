# Finite diagnostics

Run the deterministic checks from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_model.py
```

The script writes [results.json](results.json). The saved run used Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. It takes a few seconds in the recorded environment. These are floating-point consistency checks; the [scientific proofs](../science/reset_theorem.md) establish the arbitrary-size theorem.

## What is checked

| Comparison | Tested scope | Consequential failure it can expose |
|---|---|---|
| Full Fock GKSL evolution versus the closed one-particle equation | Two to four modes, exact Jordan-Wigner operators, two times each | Fermionic signs, rate factors, covariance convention, or an unintended Gaussian-input restriction |
| Reference-entangled input versus vacuum replacement | One reference qubit; even-parity system branches; the system input has Wick defect 1/4 | Loss of the reference marginal, incorrect half-distance convention, or misuse of occupation as a channel bound |
| Chebyshev resolvent versus direct matrix inversion | Two to 64 sites; three rate factors; five energies and selected source sites | Port sign, cofactor indices, complex branch or normalization errors |
| Lyapunov absorption versus the resolvent integral | All source sites in the finite sizes; direct quadrature at eight sites | A missing competing-dephasing hazard or Fourier/Plancherel factor |
| Absorption plus dephasing probabilities | Two to 64 sites; rate factor 1/2, 1 and 2 | Segment probability conservation or the segment-duration bound |
| Adjoint survival effect | Eight to 64 sites; the same rate window; time 4N | A claim based only on localized inputs rather than the worst coherent one-particle input |
| Exact parity-kick generator identity | Two to four Fock modes | Incorrect transfer of the Gaussian converse to the non-Gaussian averaged channel |
| Deterministic Gaussian phase-kick branches | Two to four modes; two prescribed kick records; maximally mixed and fully occupied inputs | The loss-action determinant identity, Gaussian vacuum formula, or either finite-time witness bound |
| Native slow coherent mode | 16 to 128 sites without dephasing | A missing factor of two between amplitude damping and one-particle population survival |

The reference test uses a state of the form (vacuum with reference 0 + an even occupied pattern with reference 1)/sqrt(2). Its system marginal violates Gaussian Wick factorization by 1/4. The closure check therefore tests an allowed non-Gaussian system input. The trace distance is checked for this explicit input; the script does not compute or optimize the full diamond norm.

## Recorded observations

The largest one-particle closure error in the saved Fock checks is below 2e-16. The largest direct-resolvent discrepancy is below 3e-14, and the largest segment conservation discrepancy is below 7e-14.

At 64 sites and time 4N, the maximum survival over all coherent one-particle inputs is:

| Dephasing rate | Survival norm |
|---|---:|
| (1/2)/N | 0.390087 |
| 1/N | 0.222770 |
| 2/N | 0.155659 |

For rate 1/N, the analytic absorption lower constant is approximately 0.0105641. The directly evaluated minimum site absorption probability at 64 sites is approximately 0.324131. The proof deliberately uses a conservative bound.

The native slowest population-decay rate multiplied by N^3 rises from 13.5592 at 16 sites to 15.4975 at 128 sites, consistent with the derived limiting value 8 pi^2/5, approximately 15.7914. This finite sequence supports the rate convention; it does not prove an asymptotic law.

## Two different noise descriptions

The upper proof uses projective one-particle dephasing events because they localize a surviving particle. The lower proof uses the exact identity

```math
\gamma\mathcal D[n_j](\rho)
=\frac\gamma4(Z_j\rho Z_j-\rho),
\qquad Z_j=I-2n_j=e^{i\pi n_j}.
```

Its Poisson phase-flip trajectories are Gaussian. Projective-jump trajectories need not be Gaussian. The checks compare the two unconditional generators exactly in finite Fock space and test the Gaussian attenuation formulas on prescribed phase-flip records. They do not treat a sampled trajectory average as proof of the identity.

## Hosted mathematics

The [read-only capture workflow](../.github/workflows/hosted-math.yml) opens the exact proposed GitHub revision at desktop and narrower widths. It compares each accessible MathML structure with MathJax compiled from that same source, checks expression text and display geometry, and retains HTML, screenshots and reports as a CI artifact. The [capture helpers](hosted_math/capture_hosted_math.cjs) and [text checker](hosted_math/check_rendered_math.py) can also run locally with Playwright, Chromium and MathJax. The workflow uses pinned actions, grants only content read access, and does not execute on external-fork pull requests.

This checks rendering and source correspondence. It does not establish the scientific claims, and screenshot review remains necessary to assess readability. Artifacts have a fourteen-day retention period; the mathematical source and reproduction scripts remain in the repository.

## Limits

No interval arithmetic, optimal finite-N constant, cutoff profile, disorder tolerance, finite-temperature extension or hardware noise-generation cost is certified. The finite time 4N survival check is stronger than the conservative analytical block constant in these samples; it is not substituted for that proof constant. A finite rate window does not give uniform constants as its endpoints approach zero or infinity. The script does not establish priority or an unrestricted quantum-over-classical advantage.
