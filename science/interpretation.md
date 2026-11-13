# Physical meaning and resource accounting

## Why adding noise helps this reset task

The hopping Hamiltonian transports many wave packets ballistically, but universal initialization must also handle specially chosen coherent states. Near a band edge, a native eigenmode has very small endpoint amplitude. One boundary sink then sees that mode only on a time scale proportional to the cube of the chain length. An initially localized excitation is a mixture of many band components and is a different benchmark.

Onsite number dephasing leaves the total particle number unchanged. It can nevertheless destroy the coherent mode structure that shields a particle from the sink. In the one-particle projector-jump description, each dephasing event selects a site; the time to the next such event is of order the chain length when $`\gamma=b/N`$. The resolvent estimate proves a positive chance of absorption during every resulting segment. It is this uniform regenerative probability, rather than a spectral gap alone, that supplies the complete reset guarantee.

## What the complete channel criterion adds

Let $`\mathcal R_0`$ replace the system by its global vacuum. Half-diamond error at most $`\epsilon`$ means that for every joint initial state $`\rho_{SR}`$,

```math
\frac12\left\Vert 
(\mathcal E_t\otimes\mathrm{id}_R)(\rho_{SR})
-|\mathrm{vac}\rangle\langle\mathrm{vac}|\otimes\rho_R
\right\Vert _1\le\epsilon.
```

The criterion controls the entire register and arbitrary correlations with an external reference. A small occupation at one selected site or a small density per site would allow a substantial probability that some unwanted particle remains. The expected-particle bound must therefore decrease by a factor proportional to $`N`$. That requirement produces the logarithm, and the inherited determinant converse shows that it cannot be removed within the stated randomized quadratic class.

No Gaussian input promise is used in the upper bound. The occupation matrix closes under the full Lindblad evolution even when the many-body state is nonGaussian. Its closed equation is sufficient because the vacuum is a pure target and nonvacuum probability is bounded by the total expected particle number.

## Independent noise and two unravelings

The upper bound uses the one-particle localization representation. The lower uses an equivalent phase-flip representation. For $`n_j^2=n_j`$, define $`Z_j=I-2n_j=e^{i\pi n_j}`$. Then

```math
\gamma\mathcal D[n_j]
=\frac\gamma4\mathcal D[Z_j],
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

The right side is a Poisson process of Gaussian onsite phase flips. Each trajectory has exactly the same boundary loss action. The ensemble state need not be Gaussian, but the inherited Gaussian determinant barrier applies on every phase-flip trajectory and survives averaging. Projective localization trajectories themselves are not used for that lower-bound argument.

Independent onsite noise is material. A single globally correlated jump proportional to total particle number would act as a scalar in the one-particle sector and would not provide the localization mechanism.

## Counted physical resources

| Resource | Supplied architecture |
|---|---|
| Quantum register | $`N`$ fermionic modes on a path |
| Coherent couplings | $`N-1`$ identical nearest-neighbor hopping terms of unit strength |
| Particle-removing interface | One unit-rate vacuum-loss port at one endpoint |
| Phase noise | $`N`$ independent onsite number-dephasing terms, each at rate $`b/N`$ |
| Sum of dephasing coefficients | $`b`$, independent of the chain length |
| Dynamics | Static, time-independent Lindblad generator |
| Performance cost | Elapsed physical time, with all losses and phase-noise evolution included |

The inverse-size per-site rate can be miscalibrated by a fixed factor while remaining in a fixed interval $`b\in[b_-,b_+]`$ with $`0\lt b_-\le b_+\lt \infty`$. The reset order is uniform on such an interval. This is a homogeneous-rate tolerance statement; it does not assert tolerance of arbitrary spatial disorder or correlated noise.

With hopping angular frequency $`J`$ and matched loss rate $`\kappa=J`$, rescaling time gives $`\gamma=bJ/N`$ and physical reset time $`\Theta_b(J^{-1}N\log(N/\epsilon))`$. The local hopping strength is bounded, while the total Hamiltonian strength grows with the number of bonds. No fixed total Hamiltonian budget is imposed.

## How to read the comparison

The clean noisy chain has a matching reset law. For the identical chain with dephasing removed, an explicit long-lived eigenmode gives a cubic lower bound. This establishes the autonomous speedup without assuming that an inverse spectral gap automatically equals a complete mixing time. The [native comparison](native_comparator.md) states precisely which upper and lower conclusions are proved.

The resource-class optimum comes from the established loss-action converse in [Fermionic Reset Complexity](https://github.com/GoGoKo699/Fermionic-Reset-Complexity/blob/7cc91ccf5f1e7b503a95105b6d0b6885e1088349/science/gaussian_bound.md). Active mode reshuffling or specially engineered couplings are different implementations of coherent transport. Interacting entropy compression can attain linear action and lies outside the noninteracting comparison class here.

Finally, number dephasing conserves particles but need not conserve the hopping energy: $`[H,n_j]\ne0`$. The result counts bath coefficients and elapsed time, without assigning a heat, work or apparatus-construction cost to the phase baths. The initial bath is ideal vacuum; nonzero injection changes the reset target and requires a new analysis.

[Return to the scientific route](README.md).
