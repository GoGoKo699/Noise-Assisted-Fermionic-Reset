# From open-system dynamics to complete chain reset

A boundary sink removes a particle only when the particle reaches it. A long chain has coherent states that scarcely visit that endpoint. This project shows how weak, independent onsite phase noise removes that protection and resets the entire register in order $`N\log(N/\epsilon)`$ time. Reset includes correlations with an arbitrary external reference.

The single educational anchor is Ángel Rivas and Susana F. Huelga, **Open Quantum Systems: An Introduction**, Springer, 2012. Use the [author preprint, arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2), revised **9 February 2012**. The [publisher record](https://doi.org/10.1007/978-3-642-23354-8) identifies the same book. All section and page locators below refer to the numbered pages of that preprint; its section numbering differs from the published book's chapter numbering.

This bridge supplies the project-specific steps after the anchor's channel and generator foundations. The [30-milestone map](MILESTONES.md) organizes the understanding targets, while the [scientific account](../science/README.md) contains the complete proofs.

## From the anchor to the chain

| Preprint locator | Foundation to take from it | Step supplied here |
|---|---|---|
| §2.2, p.6; §2.3, p.8; §2.3.1, p.11 | Operator exponentials, semigroup composition, contractivity | Apply composition to a killed one-particle process and repeat a uniform survival bound |
| §4.1, p.23 | Reduced dynamics and dependence on initial system–bath correlations | Fix the bath model independently of the unknown register input |
| §4.2, p.26, especially Eqs.35–36 | Channels acting consistently on arbitrary inputs and spectator systems | Define reset on the system together with an untouched reference |
| §4.3, p.29 | Trace norm contraction | Convert a vacuum-probability estimate into a reference-sensitive error bound |
| §4.5, p.33 | Temporal composition in Markovian evolution | Use the same autonomous semigroup after every survival block |
| §5.2, p.37, Theorem5.1 and Eq.46 | The positive-rate GKSL generator form | Insert the hopping, loss and number-dephasing operators with the correct factors |
| §5.4, pp.45–46, especially Theorem5.4 on p.46 | Stationary states and qualitative relaxation | Distinguish eventual convergence from a size-uniform reset time |

The source locators identify foundations, not claims that the book proves this chain theorem. CAR occupation closure, the two unravelings, the resolvent estimate, the renewal bound, diamond-norm reset and the determinant converse are developed below and in the linked project proofs.

The main notation translations are:

| Anchor notation | Project notation and meaning |
|---|---|
| $`E_{(t_1,t_0)}`$, or a homogeneous $`E_t`$ | $`\Phi_{N,b,t}=e^{t\mathcal L_{N,b}}`$ on the full register |
| Generator $`L_t`$ | The time-independent superoperator $`\mathcal L_{N,b}`$ |
| A term $`\gamma_k\mathcal D[V_k]`$ | Either leave its positive rate outside, or set $`L_k=\sqrt{\gamma_k}V_k`$ |
| Identity superoperator or operator denoted by $`1`$ | $`\mathrm{id}`$ for a channel and $`I`$ for a Hilbert-space operator |
| A Hilbert-space dimension often denoted by $`N`$ | Here $`N`$ counts modes; the full Hilbert-space dimension is $`2^N`$ |

In particular, the noise term is $`\gamma\mathcal D[n_j]`$ with $`\gamma=b/N`$. Coherence between two different one-particle sites decays at rate $`\gamma`$: both onsite baths contribute. Vacuum–occupied coherence of a single mode instead has dephasing rate $`\gamma/2`$, as the next example shows. The [model](../science/model.md) fixes the convention throughout.

## A one-mode example

For one mode there is no hopping. Put $`c=|0\rangle\langle1|`$, $`n=|1\rangle\langle1|`$ and use the generator $`\mathcal D[c]+\gamma\mathcal D[n]`$. Direct substitution gives

```math
\dot\rho_{11}=-\rho_{11},\qquad
\dot\rho_{01}=-\frac{1+\gamma}{2}\rho_{01}.
```

With $`q=e^{-t}`$ and $`\eta=e^{-(1+\gamma)t/2}`$, the exact channel is

```math
\Phi_t(\rho)=\begin{pmatrix}
\rho_{00}+(1-q)\rho_{11}&\eta\rho_{01}\\
\eta\rho_{10}&q\rho_{11}
\end{pmatrix}.
```

The excited input has residual particle probability $`q`$, independent of the dephasing rate. Adding phase noise cannot make a particle leave a single isolated lossy site faster. The chain advantage concerns coherent transport to that site.

Now retain a reference qubit and start with $`(|00\rangle+|11\rangle)/\sqrt2`$, with the system listed first. The output is

```math
\begin{aligned}
\omega_{SR}=\frac12\bigl[&
 |00\rangle\langle00|+(1-q)|01\rangle\langle01|\\
&+q|11\rangle\langle11|\\
&+\eta(|00\rangle\langle11|+|11\rangle\langle00|)\bigr].
\end{aligned}
```

The target is $`|0\rangle\langle0|\otimes I_R/2`$. Diagonalizing the $`|00\rangle,|11\rangle`$ block of their difference gives the exact half trace distance

```math
\begin{aligned}
&\frac12\|\omega_{SR}-|0\rangle\langle0|\otimes I_R/2\|_1\\
&\qquad=\frac{q+\sqrt{q^2+4\eta^2}}4.
\end{aligned}
```

The expected system particle number is only $`q/2`$. The error also contains the remaining joint coherence $`\eta`$. This is why the many-body proof must explain how small occupation controls correlations, rather than identifying occupation with channel error.

## Occupation closure without Gaussian inputs

The fermionic anticommutation relations encode the restriction that each mode has occupation zero or one. For the occupation matrix

```math
C_{k\ell}=\mathrm{Tr}(\rho c_\ell^\dagger c_k),
```

they imply $`0\preceq C\preceq I`$ and $`\mathrm{Tr}\,C\le N`$. These inequalities hold for every many-body state, including entangled and non-Gaussian states.

To see why the equation closes, use

```math
\begin{aligned}
[n_j,c_k]&=-\delta_{jk}c_k,\\
[n_j,c_\ell^\dagger]&=\delta_{j\ell}c_\ell^\dagger,\\
\mathcal D[n_j]^*(O)&=-\frac12[n_j,[n_j,O]].
\end{aligned}
```

Thus $`c_\ell^\dagger c_k`$ remains proportional to itself under each double commutator. Summing over sites leaves diagonal occupations unchanged and damps every off-diagonal entry at rate $`\gamma`$. Hopping and loss also map quadratic observables to quadratic observables. Together they give

```math
\dot C=-i[h_N,C]-\frac12\{P,C\}
 -\gamma(C-\mathrm{diag}\,C),\qquad P=|1\rangle\langle1|.
```

Closure is a statement about a set of observables. It does not say the full state remains Gaussian. This distinction allows the one-particle calculation to constrain every initial register state. See [the derivation](../science/model.md#one-body-equation-without-a-gaussian-input-assumption).

## Two unravelings with different proof jobs

A Lindblad generator can have different exact stochastic representations. Their averages describe the same unobserved channel, while the individual trajectories serve different mathematical purposes here.

| Representation | Event and rate | Useful property |
|---|---|---|
| One-particle projector jumps | $`\sqrt\gamma P_j`$; total event rate $`\gamma=b/N`$ while the particle survives | An event leaves a site state, which starts a new absorption segment |
| Full-register phase flips | $`Z_j=I-2n_j`$ at Poisson rate $`\gamma/4`$ per site; total rate $`b/4`$ | Every phase flip is a number-conserving Gaussian unitary |

The second representation follows by expanding the exact identity

```math
\gamma\mathcal D[n_j](\rho)
=\frac\gamma4(Z_j\rho Z_j-\rho).
```

The different event rates are consistent: the representations assign different meanings to an event. Projector trajectories are convenient for the upper bound; phase-flip trajectories preserve the structure needed for the lower bound. Neither record is available to a controller. In particular, the upper proof does not introduce monitored feedback, and the lower proof does not treat projective localization as a Gaussian unitary.

## From a resolvent to repeated absorption

Ignore dephasing temporarily and let

```math
K_t=e^{(-ih_N-P/2)t}.
```

For a particle starting at $`j`$, $`|(K_t)_{1j}|^2dt`$ is the unnormalized probability of absorption in a short time interval. Competing dephasing occurs at rate $`\gamma`$, so the probability of reaching the sink before the next localization is

```math
p_j=\int_0^\infty e^{-\gamma t}|(K_t)_{1j}|^2dt.
```

The Fourier transform of the exponentially damped propagator turns this integral into a Green-function expression:

```math
p_j=\frac1{2\pi}\int_{\mathbb R}
\left|\left[(E+i\gamma/2)I-h_N+iP/2\right]^{-1}_{1j}\right|^2dE.
```

A path tridiagonal determinant obeys a two-term recurrence, so Chebyshev polynomials give its inverse entry explicitly. The [absorption proof](../science/absorption.md) integrates a central frequency band. On that band the imaginary part of the propagation phase is of order $`\gamma`$. Because $`N\gamma=b`$ stays bounded, propagation over the whole chain introduces a bounded attenuation factor. Averaging the oscillating numerator over this band then gives $`p_j\ge a_b>0`$ uniformly in the starting site and chain length.

Each segment ends either at absorption or at a localization event. Its mean duration is at most $`1/\gamma=N/b`$. After the first localization, every new segment has success probability at least $`a_b`$, regardless of the previous site history. Conditional iteration gives a geometric tail, even though the site labels need not be independent. Therefore

```math
\sup_\rho\mathbb E_\rho\tau_{\rm abs}
\le\frac Nb(1+a_b^{-1})=C_bN.
```

The first segment can start in an arbitrary coherent state. Markov's inequality gives survival at most $`1/2`$ after $`2C_bN`$. Repeating the same bound at successive block boundaries gives survival at most $`2^{-k}`$ after $`k`$ blocks. The semigroup property from the anchor supplies composition; the project-specific resolvent and renewal estimates supply a uniform contraction to compose.

## From vacuum probability to reference reset

There are at most $`N`$ initial particles. By occupation closure and the uniform one-particle bound,

```math
\mathbb E\widehat N(t)\le N2^{-k},\qquad t=2C_bNk.
```

The operator inequality $`I-|\Omega_N\rangle\langle\Omega_N|\preceq\widehat N`$ then bounds the nonvacuum probability by $`\delta=N2^{-k}`$. This remains true for the system marginal of any reference-entangled input.

The missing reference step is gentle vacuum projection. For an output $`\omega_{SR}`$, let $`P_0=|\Omega_N\rangle\langle\Omega_N|\otimes I_R`$. A nonvacuum probability at most $`\delta`$ implies

```math
\|\omega-P_0\omega P_0\|_1\le2\sqrt\delta.
```

One way to see the square root is to purify $`\omega`$: the removed component of the purification has vector norm at most $`\sqrt\delta`$. The trace norm between its original rank-one operator and the unnormalized projected rank-one operator is at most twice that value. Taking a partial trace preserves the bound.

The projected state has the form $`|\Omega_N\rangle\langle\Omega_N|\otimes\omega_R^0`$. Its missing reference marginal is positive with trace at most $`\delta`$. Since a system channel leaves $`\rho_R`$ unchanged, the triangle inequality gives

```math
\frac12\|\omega_{SR}
 -|\Omega_N\rangle\langle\Omega_N|\otimes\rho_R\|_1
\le\sqrt\delta+\frac\delta2.
```

This is uniform over all inputs and references, and hence bounds half the diamond norm. Taking $`\delta\le\epsilon^2/4`$ needs $`k=O[\log(N/\epsilon)]`$ blocks. The complete upper bound is therefore $`O_b[N\log(N/\epsilon)]`$. The anchor motivates reference-compatible dynamics; this projection argument supplies the additional quantitative channel estimate.

## Why the determinant forces a logarithm

For the lower bound, use the phase-flip representation and start with all modes occupied. Conditional on a phase-flip record, the channel is Gaussian vacuum attenuation with one-particle matrix $`K_\omega`$. Unit-rate loss acts for elapsed time $`t`$ on every record, while phase kicks have determinant modulus one. Hence

```math
\det(K_\omega^\dagger K_\omega)=e^{-t}.
```

If $`s_i`$ are the squared singular values of $`K_\omega`$, their product is fixed. The conditional vacuum probability is $`\prod_i(1-s_i)`$. Concavity of $`x\mapsto\log(1-e^x)`$ shows this product is largest when the remaining attenuation is evenly shared:

```math
P_{\rm vac}(t\mid\omega)
\le(1-e^{-t/N})^N.
```

The bound survives averaging. Even in the most favorable equalized case, $`N`$ residual occupation factors compound into a global failure probability. Keeping that failure bounded requires $`e^{-t/N}`$ of order $`1/N`$, or $`t`$ of order $`N\log N`$. Keeping the error explicit gives $`\Omega[N\log(N/\epsilon)]`$.

This converse specializes the established Gaussian loss-action obstruction in [Fermionic Reset Complexity](../references/RELATED_WORK.md). It is an inherited research ingredient, not an additional educational anchor. The [reset proof](../science/reset_theorem.md#lower-bound-the-single-port-determinant-barrier) gives the exact finite-time witness and the scope of the number-conserving argument.

## Native comparison and final synthesis

The anchor's stationary-state discussion separates relaxation from stationarity, and its spectral treatment explains why decay modes matter. For this particular chain, the [native comparison](../science/native_comparator.md) constructs an eigenmode whose probability-decay rate is order $`N^{-3}`$. That is an allowed initial state, so it directly forces a cubic reset lower bound when dephasing is absent. A spectral gap by itself is not used to infer a whole-channel upper bound.

The result joins five distinct steps: weak phase noise supplies localization, the resolvent supplies a uniform absorption chance, renewal handles every coherent one-particle input, occupation plus gentle projection handles the whole register and every reference, and the inherited determinant mechanism matches the required logarithm. For $`\gamma=b/N`$ and fixed positive $`b`$,

```math
t_{N,b}(\epsilon)=\Theta_b\!\left(N\log\frac N\epsilon\right),
\qquad N\ge1,\quad 0\lt\epsilon\le\frac12.
```

The statement is uniform on fixed positive compact intervals of $`b`$. It counts the added independent phase baths and elapsed time. It does not establish robustness to arbitrary disorder, finite-temperature injection, or correlated onsite noise, and it does not assign a thermodynamic cost to engineering those baths. The [interpretation](../science/interpretation.md) connects these limits to initialization.
