# Relationship to earlier work

[Repository](../README.md) · [References](REFERENCES.md)

## The contribution after the known ingredients are credited

The hopping Hamiltonian, onsite number dephasing, boundary loss, closed equations for two-point functions, and noise-assisted transport mechanism all have established precedents. This project uses those ingredients to prove a complete reset guarantee for one fixed, spatially local architecture.

Set the nearest-neighbor hopping and single boundary-loss strengths to one and the onsite dephasing rate to $\gamma=1/N$. The resulting time-independent channel resets every input, including inputs entangled with an arbitrary reference, in time of order $N\log(N/\varepsilon)$ for $0<\varepsilon\le1/2$. A trajectory-wise determinant bound supplies the matching order. With dephasing removed and the same native Hamiltonian and sink retained, a slow one-particle state gives a cubic lower bound at fixed error. A matching cubic upper bound for that native channel is not part of the result.

The specific upper-bound step developed here is a uniform lower bound on the probability of absorption **before the next dephasing localization**, starting at any site. A finite-path resolvent estimate proves that bound at a dephasing rate that decreases with system size. A regenerative argument then controls the survival of every initial one-particle state. Two-point closure and a vacuum-projection estimate lift that control to the full replacement channel. The argument does not turn an asymptotic spectral gap into a mixing-time assertion.

## The closest dephasing-chain accounts

**Alba [Alba25](REFERENCES.md#alba25) studies essentially the same correlation dynamics.** The paper treats uniform hopping, onsite number dephasing, and loss at the two ends; it also identifies the unequal-boundary-rate variation. Its Bethe ansatz constructs the spectrum and eigenvectors of the two-point generator and describes the diffusive band and late density evolution. The shared model and its exact correlation analysis are credited here.

The displayed large-size gap expansion and density asymptotics keep the noise parameters fixed and use their stated asymptotic assumptions. They do not by themselves give a size-uniform survival estimate after substituting $\gamma=1/N$, nor a matching complete-register reset law. The present proof addresses that joint weak-noise/large-size regime directly. Changing two sinks to one is an architectural choice, not the sole basis of the contribution.

**Turkeshi and Schiró [TS21](REFERENCES.md#ts21) supply particularly close tools.** They study uniform spinless hopping with bulk dephasing, particle injection at one end, and extraction at the other. Their stationary task concerns current, density profiles, and Green functions. Section III.1 gives two-point closure despite the non-Gaussian averaged state. Section III.2, Eqs. (30)–(34), gives finite-path tridiagonal resolvents with imaginary broadening and boundary terms; Section III.4 discusses the quadratic noisy-Hamiltonian unraveling. Those methods are credited here. The added conclusion is the uniform absorption estimate and its complete-reset consequence, rather than a new solvability method or stationary transport formula.

More generally, Hermitian quadratic jumps need not preserve Gaussian states even when the equations for correlation functions close. This distinction is part of the established quadratic-Lindblad framework [BZ22](REFERENCES.md#bz22). Exact dephasing-chain spectral methods also precede these boundary analyses [MEP16](REFERENCES.md#mep16). The upper proof therefore applies the closed particle-number equation to arbitrary states; it does not assume that the many-body channel is Gaussian.

## Weak noise and fast mixing are established ideas

Žnidarič [Z15](REFERENCES.md#z15), Sec. III.A, analyzes the XX chain with bulk dephasing and identifies an inverse-length crossover scale between weak-noise and diffusive spectral behavior. The same paper studies cubic gap scaling in boundary-dissipated integrable chains. Thus an inverse-length useful dephasing scale, and the presence of slow coherent boundary modes, are inherited physical insights. The bulk-only model conserves particle number and does not reset to vacuum; its spectral conclusions are not the uniform survival estimate used here. Rate conventions differ, so numerical coefficients are not transferred between generators without conversion.

Fedichkin, Solenov, and Tamon [FST06](REFERENCES.md#fst06) derive low- and high-decoherence mixing behavior for continuously monitored quantum walks on cycles. Richter [R07](REFERENCES.md#r07) establishes fast mixing of decoherent walks on periodic lattices and explains robustness under different measurement-time distributions. These works already show that suitable decoherence can improve quantum-walk mixing. Their output is a position distribution approaching uniformity, rather than complete many-fermion replacement through a persistent vacuum sink. The present result does not claim the first noise-assisted relaxation mechanism or the first useful inverse-length noise rate.

## Excitation transfer and complete reset ask different questions

Plenio and Huelga [PH08](REFERENCES.md#ph08) establish dephasing-assisted excitation transfer in quantum networks. Their uniform-chain discussion considers an excitation initially localized at one end and measures the population delivered to a sink. In that task they found no dephasing benefit in the stated finite-chain searches and gave short-chain analytical checks. This does not conflict with the reset result: a worst-input replacement-channel task also includes slowly absorbed coherent mode states and extensively occupied inputs. No claim is made that dephasing improves every localized excitation-transfer experiment.

Zhang, Celardo, Borgonovi, and Kaplan [ZCBK17](REFERENCES.md#zcbk17) further analyze ballistic transfer in disordered chains and already find inverse-length or inverse-square-root-length optimal dephasing scales in different regimes. Their result concerns a different transfer objective and does not supply the whole-register reset bound.

Riberi [R26](REFERENCES.md#r26) solves a coherent half-line walk with a Lindblad boundary sink, including its exact propagator, absorption statistics, and boundary-localized mode. It provides a close analytic account of the lossy endpoint. The present finite-chain bound includes repeated bulk localization and controls all initial states; it is not an assertion about the half-line walk's total absorption probability.

## The reset lower bound is inherited

The public scientific account **Fermionic Reset Complexity** [FRC](REFERENCES.md#frc) proves that Gaussian reset through a single vacuum-loss port needs damping action of order $N\log N$ at fixed global error, allowing arbitrary prescribed quadratic control and input-independent classical randomization. Its construction attains that order by equal mode exposure, with coherent synthesis and locality unpriced.

The logarithmic bottleneck is therefore not a new discovery of this project. Here, the same determinant mechanism is specialized to number-conserving stochastic phase trajectories. A fully occupied input gives an explicit lower bound with the dependence $N\log(N/\varepsilon)$. Averaging the trajectories preserves the population bound even though the resulting state can be non-Gaussian.

The additional capability is attaining that reset order with fixed nearest-neighbor hopping, one continuously active sink, and unobserved onsite dephasing, without active mode permutations or access to noise records. This is a local autonomous realization of the known resource order. It is not a separation from all noiseless control protocols.

**Boundary Memory Erasure** [BME](REFERENCES.md#bme) is another related public account, but its carrier is a constrained qutrit chain: vacancies and two spin labels, with the ordered spin word preserved by hopping. Its final erasure target is completely mixed, and its drain/refill and filling-threshold results depend on that spin-order memory. The present spinless fermion model instead targets the vacuum and supplies bulk dephasing. Neither theorem is transferred to the other's model.

## Scope of the comparison

This comparison uses the primary versions and pinned public accounts identified in the [reference list](REFERENCES.md). It supports the stated relationship to those sources, rather than an exhaustive priority claim. The result assigns a reset time in an ideal Markovian model. It does not establish a heat or work advantage, an efficient method for generating the noise, or superiority over arbitrary classical or interacting reset architectures.

