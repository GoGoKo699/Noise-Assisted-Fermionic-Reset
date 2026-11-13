# Thirty milestones for noise-assisted complete reset

[Learning route](README.md) · [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md) · [Scientific route](../science/README.md)

This is a shared map of the project's understanding targets. It contains **exactly 30 milestones: 14 background/preliminaries milestones and 16 narrative/innovation milestones**. The background moves from one register and its noise terms to the complete reset framework. The narrative first identifies the native obstruction, then joins the local absorption estimate to the full-channel upper bound, the inherited converse, and the physical conclusion.

The selected anchor is Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction* (2012), using the authors' [arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2), revised 9 February 2012. **RH** below refers to that preprint's section numbering and printed page numbers, as verified in the [source bridge](RIVAS_HUELGA_BRIDGE.md). These locators are not substituted for the published book's chapter numbering.

The anchor supports channels, contractions, semigroups, generators, and stationary-state context. Fermionic CAR, the ordinary diamond norm, the path resolvent, conditional renewal, and the Gaussian determinant argument are supplied by the project's scientific account and the bridge. A source pointer marked “supporting context” does not attribute the specialized project theorem to the book.

| Phase | Milestones | Role in the story |
|---|---|---|
| Background/preliminaries | M01–M14 | Assemble the register, complete-channel task, local dynamics, and tools needed to state the argument. |
| Narrative/innovation | M15–M30 | Connect the native slow mode, absorption mechanism, two reset bounds, and scoped physical contribution. |

The milestones express conceptual understanding, dependencies, and scientific source routes. Specialist calculations remain in the linked proof pages.

## M01 Register and vacuum

**Phase:** Background/preliminaries.

**Central question:** What does it mean to empty this quantum register?

**Understanding target:** Identify the $`N`$ modes, their occupation basis, the $`2^N`$-dimensional register, and the unique global vacuum. Distinguish that vacuum target from a small density of particles.

**Dependencies and story role:** None. Establishes the physical object and target before introducing dynamics or accuracy.

**Conceptual connection:** A local vacancy is a basis state; complete initialization is a statement about the state of the entire register.

**Source pointers:** Anchor: RH §4.1 (p. 23), dynamical-map context; the fermionic register is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-the-anchor-to-the-chain). Project: [Register and fixed generator](../science/model.md#register-and-fixed-generator) · [Complete-channel meaning](../science/interpretation.md#what-the-complete-channel-criterion-adds).

## M02 States, references, and channels

**Phase:** Background/preliminaries.

**Central question:** Which information must reset remove when the register is correlated with something else?

**Understanding target:** Explain the replacement map $`\mathcal R_N`$ and why its correct joint output is vacuum tensored with the original reference marginal. Recognize that a system-only operation cannot change that marginal.

**Dependencies and story role:** [M01](#m01-register-and-vacuum). Turns an empty-register target into an input-independent channel task.

**Conceptual connection:** Complete positivity describes consistent action on a subsystem; a reference exposes information that a system-only fidelity test can miss.

**Source pointers:** Anchor: RH §§4.1–4.2 (pp. 23, 26). [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-the-anchor-to-the-chain). Project: [Error and elapsed time](../science/model.md#error-and-elapsed-time) · [Reference criterion](../science/interpretation.md#what-the-complete-channel-criterion-adds).

## M03 Trace and diamond global error

**Phase:** Background/preliminaries.

**Central question:** How is complete reset accuracy measured?

**Understanding target:** Distinguish half trace distance for states, half diamond distance for channels, and local occupation error. Explain why the supremum over joint inputs makes the reset guarantee uniform.

**Dependencies and story role:** [M02](#m02-states-references-and-channels). Fixes the global success criterion used by every later upper and lower bound.

**Conceptual connection:** Trace-norm contraction under physical maps supports error comparison; extending the test by an identity channel motivates the reference-sensitive channel norm.

**Source pointers:** Anchor: RH §4.3 (p. 29) for contraction; the diamond-norm criterion is additional project material. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-vacuum-probability-to-reference-reset). Project: [Error definition](../science/model.md#error-and-elapsed-time) · [Complete reset theorem](../science/reset_theorem.md#theorem).

## M04 CAR and occupation

**Phase:** Background/preliminaries.

**Central question:** Why is the one-body occupation matrix physically bounded?

**Understanding target:** Interpret the canonical anticommutation relations and explain $`0\preceq C\preceq I`$, $`\mathrm{Tr}\,C\le N`$, and the equality between its trace and expected total particle number.

**Dependencies and story role:** [M01](#m01-register-and-vacuum), [M02](#m02-states-references-and-channels). Supplies the many-body-to-one-body quantities needed for the later lift.

**Conceptual connection:** Fermionic exclusion bounds the spectrum of the occupation matrix even when the full state has arbitrary correlations.

**Source pointers:** Anchor: RH §5.2 (p. 37) for generator context; CAR and occupation bounds are supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#occupation-closure-without-gaussian-inputs). Project: [One-body equation](../science/model.md#one-body-equation-without-a-gaussian-input-assumption).

## M05 Hopping and slow modes

**Phase:** Background/preliminaries.

**Central question:** Why can ballistic hopping coexist with slow boundary removal?

**Understanding target:** Relate the path hopping matrix to coherent propagation and distinguish a localized excitation from a coherent mode with little endpoint weight. Understand why a worst-input reset task must include both.

**Dependencies and story role:** [M04](#m04-car-and-occupation). Reveals the obstruction that the added dephasing must remove.

**Conceptual connection:** Propagation speed of typical wave packets does not determine the visibility of every coherent state to one local sink.

**Source pointers:** Anchor: RH §2.2 (p. 6) for operator exponentials and §5.2 (p. 37) for Hamiltonian evolution. [Source bridge](RIVAS_HUELGA_BRIDGE.md#native-comparison-and-final-synthesis). Project: [Fixed hopping model](../science/model.md#register-and-fixed-generator) · [Physical mechanism](../science/interpretation.md#why-adding-noise-helps-this-reset-task).

## M06 CP semigroups and GKSL

**Phase:** Background/preliminaries.

**Central question:** What makes this static master equation a physical Markov evolution?

**Understanding target:** Connect the GKSL form to a time-homogeneous completely positive, trace-preserving semigroup. Keep the physical full-register channel distinct from reduced matrices used to analyze it.

**Dependencies and story role:** [M02](#m02-states-references-and-channels), [M03](#m03-trace-and-diamond-global-error). Provides the dynamical framework into which hopping, loss, and dephasing fit.

**Conceptual connection:** A generator describes infinitesimal dynamics; its exponential supplies finite-time channels and the semigroup composition law.

**Source pointers:** Anchor: RH §§2.3, 4.5, 5.2 (pp. 8, 33, 37). [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-the-anchor-to-the-chain). Project: [Full generator](../science/model.md#register-and-fixed-generator) · [Elapsed-time channel](../science/model.md#error-and-elapsed-time).

## M07 Vacuum loss

**Phase:** Background/preliminaries.

**Central question:** What can one boundary loss port remove, and at which rate?

**Understanding target:** Read $`\mathcal D[c_1]`$ in the stated convention, identify the absorbing vacuum, and distinguish loss strength from the amount of population that coherent transport delivers to the port.

**Dependencies and story role:** [M04](#m04-car-and-occupation), [M06](#m06-cp-semigroups-and-gksl). Introduces the only particle-removing resource.

**Conceptual connection:** A local dissipator can purify a whole register only through the dynamics that expose its degrees of freedom to that dissipator.

**Source pointers:** Anchor: RH §§5.2, 5.4 (pp. 37, 45). [Source bridge](RIVAS_HUELGA_BRIDGE.md#a-one-mode-example). Project: [Generator and rate convention](../science/model.md#register-and-fixed-generator) · [Killed propagation](../science/absorption.md#absorption-before-the-next-dephasing-event).

## M08 Number dephasing

**Phase:** Background/preliminaries.

**Central question:** How can noise help empty a chain without removing particles itself?

**Understanding target:** Explain how onsite number dephasing suppresses off-diagonal occupation-matrix entries while preserving total particle number and the vacuum. Distinguish number conservation from conservation of hopping energy.

**Dependencies and story role:** [M04](#m04-car-and-occupation), [M06](#m06-cp-semigroups-and-gksl), [M07](#m07-vacuum-loss). Adds the mechanism that disrupts slowly absorbed coherent modes.

**Conceptual connection:** Removing phase coherence can alter access to a separate loss channel even though the dephasing channel does not supply the loss.

**Source pointers:** Anchor: RH §5.2 (p. 37); the number-dephasing identities and resource interpretation are supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#a-one-mode-example). Project: [One-body dephasing equation](../science/model.md#one-body-equation-without-a-gaussian-input-assumption) · [Counted resources](../science/interpretation.md#counted-physical-resources).

## M09 Unobserved unravelings

**Phase:** Background/preliminaries.

**Central question:** How can different trajectory descriptions represent the same unread channel?

**Understanding target:** Distinguish the one-particle localization representation from the full-register phase-flip representation. Explain why using either representation in a proof supplies no measurement result or feedback resource.

**Dependencies and story role:** [M06](#m06-cp-semigroups-and-gksl), [M07](#m07-vacuum-loss), [M08](#m08-number-dephasing). Establishes why the upper and lower proofs may use different stochastic descriptions.

**Conceptual connection:** A generator is a channel-level object; its trajectory labels depend on a representation and need not be operationally accessible.

**Source pointers:** Anchor: RH §5.2 (p. 37) for the generator; the two exact unravelings are additional project material. [Source bridge](RIVAS_HUELGA_BRIDGE.md#two-unravelings-with-different-proof-jobs). Project: [Two exact representations](../science/model.md#two-exact-representations-of-dephasing) · [Independent noise](../science/interpretation.md#independent-noise-and-two-unravelings).

## M10 Closure versus Gaussianity

**Phase:** Background/preliminaries.

**Central question:** What does a closed occupation equation say about a non-Gaussian state?

**Understanding target:** Explain why quadratic-observable closure is sufficient to evolve the occupation matrix for every input, but does not imply that the averaged many-body state is Gaussian. Identify where Gaussian structure will instead be used branch by branch.

**Dependencies and story role:** [M04](#m04-car-and-occupation), [M06](#m06-cp-semigroups-and-gksl), [M08](#m08-number-dephasing), [M09](#m09-unobserved-unravelings). Prevents an unjustified input restriction in the upper proof and a mistaken ensemble assumption in the lower proof.

**Conceptual connection:** A tractable hierarchy of selected observables is weaker than a complete state description.

**Source pointers:** Anchor: RH §§4.2, 5.2 (pp. 26, 37) for physical maps and generators; fermionic closure is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#occupation-closure-without-gaussian-inputs). Project: [Exact closure](../science/model.md#one-body-equation-without-a-gaussian-input-assumption) · [Attribution of correlation methods](../references/RELATED_WORK.md#the-closest-dephasing-chain-accounts).

## M11 Killed semigroups

**Phase:** Background/preliminaries.

**Central question:** What does trace loss mean in the one-particle analysis?

**Understanding target:** Interpret the positive, trace-decreasing surviving map and its dual effect on the identity. Distinguish this killed process from the full trace-preserving channel that includes the vacuum.

**Dependencies and story role:** [M06](#m06-cp-semigroups-and-gksl), [M07](#m07-vacuum-loss), [M09](#m09-unobserved-unravelings). Supplies the survival quantity that will contract uniformly.

**Conceptual connection:** Restricting to an unabsorbed sector turns an ordinary loss channel into a useful trace-decreasing analysis without introducing physical postselection.

**Source pointers:** Anchor: RH §§2.3.1, 4.3 (pp. 11, 29) for contraction context; the killed map is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-a-resolvent-to-repeated-absorption). Project: [One-particle process](../science/absorption.md) · [One-body equation](../science/model.md#one-body-equation-without-a-gaussian-input-assumption).

## M12 Green functions and Laplace transforms

**Phase:** Background/preliminaries.

**Central question:** How does a damped propagation amplitude become a resolvent integral?

**Understanding target:** Connect the matrix exponential, its Laplace/Fourier transform, and a Green-function entry. Understand why squared amplitudes integrated over time can be estimated through a real-frequency integral.

**Dependencies and story role:** [M05](#m05-hopping-and-slow-modes), [M11](#m11-killed-semigroups). Introduces the analytical tool used to bypass a spectral-gap-to-mixing inference.

**Conceptual connection:** Time-domain absorption and frequency-domain response encode the same damped linear evolution.

**Source pointers:** Anchor: RH §§2.2–2.3 (pp. 6, 8) for exponential and semigroup background; Parseval and the path resolvent are supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-a-resolvent-to-repeated-absorption). Project: [Endpoint Green function](../science/absorption.md#endpoint-green-function).

## M13 Conditional renewal

**Phase:** Background/preliminaries.

**Central question:** When does a repeated success opportunity imply a finite mean removal time?

**Understanding target:** Combine a uniform conditional success probability with a bound on conditional interval lengths. Distinguish those assumptions from independent, identically distributed site labels.

**Dependencies and story role:** [M09](#m09-unobserved-unravelings), [M11](#m11-killed-semigroups). Provides the probabilistic bridge from a local absorption opportunity to uniform long-time survival.

**Conceptual connection:** Regeneration can control a history-dependent process when every new interval obeys the same quantitative bounds.

**Source pointers:** Anchor: RH §4.5 (p. 33) for Markov-evolution context; the conditional renewal estimate is additional project material. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-a-resolvent-to-repeated-absorption). Project: [Renewal from arbitrary states](../science/absorption.md#renewal-from-arbitrary-initial-states).

## M14 Background synthesis

**Phase:** Background/preliminaries.

**Central question:** How do the physical model, accuracy criterion, and analytical reductions fit together?

**Understanding target:** Describe the complete reset task, its fixed resources, the role of unread dephasing, and the route from one-particle survival to a many-body channel statement. Keep local occupation, Gaussianity, trajectory records, and reference errors distinct.

**Dependencies and story role:** [M01](#m01-register-and-vacuum)–[M13](#m13-conditional-renewal). Integrates the background into one framework before following the new bound.

**Conceptual connection:** The project joins open-system dynamics, fermionic observables, and channel-level information removal; no one of those viewpoints alone states the entire task.

**Source pointers:** Anchor: RH §§4.2, 4.5, 5.2 (pp. 26, 33, 37). [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-the-anchor-to-the-chain). Project: [Scientific route](../science/README.md) · [Model](../science/model.md) · [Physical meaning](../science/interpretation.md).

## M15 Native cubic obstruction

**Phase:** Narrative/innovation.

**Central question:** Which explicit coherent input makes the native chain wait at least cubic time?

**Understanding target:** Follow the characteristic equation and its analytic band-edge root to a genuine slowly decaying right eigenvector. Explain why this state proves a reset lower bound without requiring an orthogonal eigenbasis or a native upper bound.

**Dependencies and story role:** [M05](#m05-hopping-and-slow-modes), [M12](#m12-green-functions-and-laplace-transforms), [M14](#m14-background-synthesis). Makes the fixed noiseless obstruction precise before showing how noise removes it.

**Conceptual connection:** A single admissible input suffices for a worst-input lower bound, while an inverse gap alone does not establish an upper bound on the whole channel.

**Source pointers:** Anchor: RH §§2.2, 5.4 (pp. 6, 45) for evolution and asymptotic-state context; the slow-mode derivation is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#native-comparison-and-final-synthesis). Project: [Native comparison](../science/native_comparator.md) · [Right-eigenvector test input](../science/native_comparator.md#the-eigenvector-is-a-valid-reset-test-input).

## M16 Localization clock

**Phase:** Narrative/innovation.

**Central question:** Why is the time to a dephasing event independent of the surviving one-particle state?

**Understanding target:** Use $`\sum_j |j\rangle\langle j|=I`$ to identify the total localization hazard $`\gamma=b/N`$. Explain the resulting interval scale and the site state created when an event occurs.

**Dependencies and story role:** [M09](#m09-unobserved-unravelings), [M11](#m11-killed-semigroups), [M14](#m14-background-synthesis). Converts the homogeneous dephasing rate into a regenerative clock.

**Conceptual connection:** The normalization of the one-particle sector makes a quantum jump's total hazard scalar even though its site label depends on the state.

**Source pointers:** Anchor: RH §5.2 (p. 37), supporting generator context. [Source bridge](RIVAS_HUELGA_BRIDGE.md#two-unravelings-with-different-proof-jobs). Project: [Localization representation](../science/model.md#two-exact-representations-of-dephasing) · [Absorption before dephasing](../science/absorption.md#absorption-before-the-next-dephasing-event).

## M17 Absorption before the jump

**Phase:** Narrative/innovation.

**Central question:** Which probability must be bounded uniformly after localization?

**Understanding target:** Interpret $`p_j=\int_0^\infty e^{-\gamma t}|(K_t)_{1j}|^2dt`$ as absorption before the next localization. Distinguish it from eventual coherent absorption or from survival of every coherent state at a fixed time.

**Dependencies and story role:** [M12](#m12-green-functions-and-laplace-transforms), [M16](#m16-localization-clock). Identifies the local probability on which the upper proof depends.

**Conceptual connection:** The exponential localization clock gives the native lossy propagator exactly the damping needed for a frequency-space estimate.

**Source pointers:** Anchor: RH §2.2 (p. 6), supporting propagation context; the competing-event probability is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-a-resolvent-to-repeated-absorption). Project: [Absorption probability](../science/absorption.md#absorption-before-the-next-dephasing-event) · [Parseval representation](../science/absorption.md#endpoint-green-function).

## M18 Chebyshev cofactor

**Phase:** Narrative/innovation.

**Central question:** Why does the endpoint Green function have a tractable finite-chain form?

**Understanding target:** Relate the tridiagonal determinant recurrence to second-kind Chebyshev polynomials and identify the endpoint-to-site cofactor. Explain why the sine ratio is an exact resolvent identity rather than a normal-mode approximation.

**Dependencies and story role:** [M05](#m05-hopping-and-slow-modes), [M12](#m12-green-functions-and-laplace-transforms), [M17](#m17-absorption-before-the-jump). Supplies the exact formula to which the uniform estimate is applied.

**Conceptual connection:** The simple spatial architecture produces a recurrence that retains the boundary loss exactly.

**Source pointers:** Anchor: RH §2.2 (p. 6), supporting finite-operator context; the Chebyshev identity is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-a-resolvent-to-repeated-absorption). Project: [Endpoint resolvent identity](../science/absorption.md#endpoint-green-function) · [Native characteristic equation](../science/native_comparator.md#characteristic-equation).

## M19 Central energy band

**Phase:** Narrative/innovation.

**Central question:** How can one extract a positive contribution that remains uniform as the chain grows?

**Understanding target:** Explain the contour parameterization in a fixed central band, the inverse-length imaginary part, and the bounded denominator and Jacobian. Recognize why a fixed positive coefficient of inverse-size dephasing permits length-independent bounds.

**Dependencies and story role:** [M18](#m18-chebyshev-cofactor). Changes an exact Green function into a controlled estimate in the relevant joint limit.

**Conceptual connection:** Uniformity follows from bounding the finite-size expression on a chosen energy interval, rather than inserting a size-dependent rate into a fixed-rate asymptotic expansion.

**Source pointers:** Anchor: RH §§2.2–2.3 (pp. 6, 8), supporting operator-evolution context; the contour estimate is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-a-resolvent-to-repeated-absorption). Project: [Central-band estimate](../science/absorption.md#a-fixed-energy-band-carries-a-uniform-probability).

## M20 Uniform absorption probability

**Phase:** Narrative/innovation.

**Central question:** Why can no localized site evade the sink throughout the next noisy segment?

**Understanding target:** Combine the positive central-band integral with the denominator bound to obtain $`p_j\ge a_b>0`$ for every site and length. Distinguish a proved uniform constant from a sharp or optimized transport probability.

**Dependencies and story role:** [M17](#m17-absorption-before-the-jump), [M18](#m18-chebyshev-cofactor), [M19](#m19-central-energy-band). Completes the load-bearing local estimate.

**Conceptual connection:** A spatially varying cofactor still carries uniformly positive integrated weight, allowing every localization outcome to serve as a fresh absorption opportunity.

**Source pointers:** Anchor: RH §2.3.1 (p. 11), supporting contraction context; the uniform probability theorem is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-a-resolvent-to-repeated-absorption). Project: [Uniform probability proof](../science/absorption.md#a-fixed-energy-band-carries-a-uniform-probability).

## M21 Renewal from every input

**Phase:** Narrative/innovation.

**Central question:** How does a localized-state bound control an initially coherent state?

**Understanding target:** Separate the first interval from later localized intervals, bound their conditional mean lengths, and use the geometric success tail. Explain why arbitrary initial coherence and correlated site labels leave the linear mean absorption bound valid.

**Dependencies and story role:** [M13](#m13-conditional-renewal), [M16](#m16-localization-clock), [M20](#m20-uniform-absorption-probability). Extends the local probability to a uniform statement about all one-particle inputs.

**Conceptual connection:** The first localization removes the need for a special initial-state promise; conditional iteration handles the subsequent random sites.

**Source pointers:** Anchor: RH §4.5 (p. 33), supporting Markov-evolution context; the renewal argument is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-a-resolvent-to-repeated-absorption). Project: [All-input renewal proof](../science/absorption.md#renewal-from-arbitrary-initial-states).

## M22 Iterated survival

**Phase:** Narrative/innovation.

**Central question:** How does a mean absorption bound become an exponential block-survival bound?

**Understanding target:** Apply Markov's inequality on a linear-time block and iterate the surviving CP semigroup. Explain why each block may start from a different normalized surviving state without invalidating the uniform estimate.

**Dependencies and story role:** [M03](#m03-trace-and-diamond-global-error), [M11](#m11-killed-semigroups), [M21](#m21-renewal-from-every-input). Produces the time-dependent survival bound used to empty an extensive register.

**Conceptual connection:** A worst-state one-block contraction can be composed even when the conditional state changes after every block.

**Source pointers:** Anchor: RH §§2.3.1, 4.3 (pp. 11, 29) for semigroup contraction. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-a-resolvent-to-repeated-absorption). Project: [Survival iteration](../science/absorption.md#renewal-from-arbitrary-initial-states).

## M23 Many-body occupation

**Phase:** Narrative/innovation.

**Central question:** How is the one-particle estimate used for an arbitrary many-body input?

**Understanding target:** Apply the closed occupation equation and the CAR bounds to control total expected particle number. Explain the factor of register size and the inequality that bounds nonvacuum probability by expected occupation.

**Dependencies and story role:** [M04](#m04-car-and-occupation), [M10](#m10-closure-versus-gaussianity), [M22](#m22-iterated-survival). Lifts the survival estimate without imposing Gaussianity or a fixed particle number on the input.

**Conceptual connection:** The vacuum is the only zero-particle state, making particle number a witness for failure of the global reset target.

**Source pointers:** Anchor: RH §5.2 (p. 37), supporting generator context; the CAR lift is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#occupation-closure-without-gaussian-inputs). Project: [Occupation closure](../science/model.md#one-body-equation-without-a-gaussian-input-assumption) · [Many-body upper bound](../science/reset_theorem.md#upper-bound-from-one-particle-survival-to-every-reference).

## M24 Reference vacuum projection

**Phase:** Narrative/innovation.

**Central question:** Why does a small nonvacuum probability also remove correlations with every reference?

**Understanding target:** Follow gentle projection onto the system vacuum and account separately for the projected reference block. Explain how trace preservation restores the original reference marginal in the desired replacement output.

**Dependencies and story role:** [M02](#m02-states-references-and-channels), [M03](#m03-trace-and-diamond-global-error), [M23](#m23-many-body-occupation). Completes the step from a particle-number witness to a channel-norm guarantee.

**Conceptual connection:** A pure system target turns near-certain vacuum occupation into approximate system–reference decoupling, with an explicit error conversion.

**Source pointers:** Anchor: RH §4.2 (p. 26) for complete-map context; the gentle-projection reference estimate is additional project material. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-vacuum-probability-to-reference-reset). Project: [Reference-sensitive projection proof](../science/reset_theorem.md#upper-bound-from-one-particle-survival-to-every-reference).

## M25 Complete upper bound

**Phase:** Narrative/innovation.

**Central question:** Where do the register-size and accuracy logarithms enter the reset time?

**Understanding target:** Choose enough linear-time blocks to make the remaining occupation at most order $`\varepsilon^2`$. Connect that choice to the full upper order $`O_b[N\log(N/\varepsilon)]`$ and distinguish its loose constants from an optimal prefactor.

**Dependencies and story role:** [M22](#m22-iterated-survival), [M23](#m23-many-body-occupation), [M24](#m24-reference-vacuum-projection). Assembles the complete achievability statement.

**Conceptual connection:** Uniform one-particle removal must be repeated long enough to clear an entire register while satisfying the reference-sensitive error criterion.

**Source pointers:** Anchor: RH §4.3 (p. 29), supporting contraction context; the reset estimate is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#from-vacuum-probability-to-reference-reset). Project: [Theorem and explicit upper bound](../science/reset_theorem.md#theorem) · [Reference lift](../science/reset_theorem.md#upper-bound-from-one-particle-survival-to-every-reference).

## M26 Phase-flip representation

**Phase:** Narrative/innovation.

**Central question:** Which equivalent description makes the lower-bound resource class visible?

**Understanding target:** Use the exact number-dephasing/phase-flip identity and its rate convention. Explain why every finite-time branch has Gaussian unitary kicks, the same loss exposure, and no supplied record.

**Dependencies and story role:** [M08](#m08-number-dephasing), [M09](#m09-unobserved-unravelings), [M10](#m10-closure-versus-gaussianity). Opens the converse proof using a representation suited to Gaussian attenuation.

**Conceptual connection:** The localization representation helps the upper bound; the phase-flip representation reveals an inherited obstruction on each trajectory of the same channel.

**Source pointers:** Anchor: RH §5.2 (p. 37), supporting generator context; the exact phase-flip identity is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#two-unravelings-with-different-proof-jobs). Project: [Two representations and rates](../science/model.md#two-exact-representations-of-dephasing) · [Trajectorywise lower bound](../science/reset_theorem.md#lower-bound-the-single-port-determinant-barrier).

## M27 Attenuation determinant

**Phase:** Narrative/innovation.

**Central question:** Which loss-exposure quantity is unchanged by the phase kicks?

**Understanding target:** Explain the fixed determinant of the one-particle attenuation matrix and the fully occupied input's branchwise vacuum probability. Keep this Gaussian branch calculation distinct from any claim that the averaged state is Gaussian.

**Dependencies and story role:** [M04](#m04-car-and-occupation), [M07](#m07-vacuum-loss), [M26](#m26-phase-flip-representation). Identifies the loss-action bottleneck that local noise cannot evade.

**Conceptual connection:** Unitary phase kicks redistribute exposure without changing its determinant budget; resetting every occupied mode requires that budget to be shared across the register.

**Source pointers:** Anchor: RH §§2.2, 5.2 (pp. 6, 37), supporting finite-evolution context; the determinant specialization is supplied by the project and its cited antecedent. [Source bridge](RIVAS_HUELGA_BRIDGE.md#why-the-determinant-forces-a-logarithm). Project: [Determinant and vacuum probability](../science/reset_theorem.md#lower-bound-the-single-port-determinant-barrier) · [Inherited Gaussian obstruction](../references/RELATED_WORK.md#the-reset-lower-bound-is-inherited).

## M28 Matching reset order

**Phase:** Narrative/innovation.

**Central question:** Why is the logarithmic overhead necessary as well as sufficient?

**Understanding target:** Use concavity to bound branchwise vacuum probability at fixed determinant, then average and test the vacuum projector. Combine the resulting lower time with the complete upper bound while preserving their different constants and witness roles.

**Dependencies and story role:** [M03](#m03-trace-and-diamond-global-error), [M25](#m25-complete-upper-bound), [M27](#m27-attenuation-determinant). Establishes the matching order rather than only an achievable protocol.

**Conceptual connection:** A selected physical input proves a channel converse; matching its order with an all-input upper identifies the resource frontier of this architecture.

**Source pointers:** Anchor: RH §4.3 (p. 29), supporting error-contraction context; the Jensen/determinant converse is additional project material. [Source bridge](RIVAS_HUELGA_BRIDGE.md#why-the-determinant-forces-a-logarithm). Project: [Lower bound](../science/reset_theorem.md#lower-bound-the-single-port-determinant-barrier) · [Uniform matching order](../science/reset_theorem.md#uniform-order-and-the-positive-rate-window).

## M29 Rate window and resources

**Phase:** Narrative/innovation.

**Central question:** Which tolerance and resource statements follow from the theorem's constants?

**Understanding target:** Explain uniformity over fixed positive compact intervals of the homogeneous inverse-size noise coefficient. Account for hopping bonds, the single loss port, total dephasing coefficient and exposure, and elapsed time; distinguish this from disorder tolerance or a heat/work claim.

**Dependencies and story role:** [M20](#m20-uniform-absorption-probability), [M25](#m25-complete-upper-bound), [M28](#m28-matching-reset-order). Reconciles the mathematical law with the resources and calibration actually supplied.

**Conceptual connection:** A useful scaling statement includes its limiting regime and charged physical resources, as well as the headline time exponent.

**Source pointers:** Anchor: RH §§5.2, 5.4 (pp. 37, 45), supporting generator and asymptotic-state context; the quantitative rate window is supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#native-comparison-and-final-synthesis). Project: [Positive rate window](../science/reset_theorem.md#uniform-order-and-the-positive-rate-window) · [Resource table](../science/interpretation.md#counted-physical-resources).

## M30 Contribution synthesis

**Phase:** Narrative/innovation.

**Central question:** What does this result add after its assumptions and closest antecedents are stated?

**Understanding target:** Connect the uniform absorption bound, complete-channel upper bound, inherited determinant converse, and native cubic obstruction into one account. Identify the added local autonomous capability and retain the limits concerning coherent controls, interactions, disorder, bath temperature, and thermodynamic cost.

**Dependencies and story role:** [M14](#m14-background-synthesis), [M15](#m15-native-cubic-obstruction), [M25](#m25-complete-upper-bound), [M28](#m28-matching-reset-order), [M29](#m29-rate-window-and-resources). Integrates both proof directions and the physical interpretation into the global contribution.

**Conceptual connection:** The result is a local autonomous realization of an established reset resource order; its scientific content is assessed at the level of the whole operational task.

**Source pointers:** Anchor: RH §§4.2, 4.5, 5.4 (pp. 26, 33, 45), supporting framework; the complete contribution and comparison are supplied by the project. [Source bridge](RIVAS_HUELGA_BRIDGE.md#native-comparison-and-final-synthesis). Project: [Scientific synthesis](../science/README.md) · [Interpretation and scope](../science/interpretation.md#how-to-read-the-comparison) · [Closest work](../references/RELATED_WORK.md).


