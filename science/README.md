# Noise-assisted complete reset on a uniform chain

A single boundary loss port can empty a uniform fermion chain very slowly. Coherent states concentrated near the edge of the hopping band have little amplitude at the lossy endpoint and survive for cubic time in the chain length. Independent phase noise destroys that long-lived mode information while leaving the vacuum unchanged.

The result concerns the complete quantum channel: after the stated time, every initial state is close to the vacuum and its correlations with any external reference have been removed. It therefore addresses initialization of the whole register, rather than the transfer efficiency of one selected excitation.

For $`N`$ modes, unit nearest-neighbor hopping and unit boundary loss, set the onsite number-dephasing rate to $`\gamma=b/N`$, with any fixed $`b>0`$. If $`t_{\rm reset}(N,\epsilon;b)`$ is the first time the half-diamond distance to vacuum replacement is at most $`\epsilon`$, then

```math
t_{\rm reset}(N,\epsilon;b)
=\Theta_b\!\left(N\log\frac{N}{\epsilon}\right),
\qquad N\ge1,\quad 0<\epsilon\le\frac12.
```

The constants can be chosen uniformly when $`b`$ lies in any fixed positive compact interval. The rate need not be tuned to one exact coefficient. The same uniform coherent chain with $`\gamma=0`$ has a worst-input lower bound of order $`N^3\log(1/\epsilon)`$.

## Follow the argument

| Scientific question | Authoritative account |
|---|---|
| Which channel, rate convention, error and resources are fixed? | [Model and statements](model.md) |
| How can one noisy particle reach a single boundary quickly from every state? | [Resolvent and absorption](absorption.md) |
| Why does particle survival control an arbitrary reference-entangled register, and why is the logarithm necessary? | [Complete reset theorem](reset_theorem.md) |
| Which exact coherent state forces a cubic native waiting time? | [Native coherent comparison](native_comparator.md) |
| What does the result mean for initialization and resource accounting? | [Physical interpretation](interpretation.md) |
| Which ingredients are inherited and what operational statement is added? | [Related work](../references/RELATED_WORK.md) |
| Which finite identities and examples can be reproduced? | [Verification](../verification/README.md) |

## Proof in one paragraph

In a one-particle representation, an unobserved dephasing jump localizes the surviving particle to a site. The endpoint Green function has an exact tridiagonal formula. Integrating a fixed central frequency band proves that, from every site, absorption at the sink occurs before the next localization with a probability bounded below independently of $`N`$. A regenerative estimate gives an $`O_b(N)`$ absorption time for every coherent one-particle input. Iteration reduces the expected remaining particle count below $`\epsilon^2`$ in $`O_b(N\log(N/\epsilon))`$ time. Gentle vacuum projection then gives the full reference-sensitive channel bound. A separate, equivalent phase-flip representation transfers the established Gaussian determinant barrier and proves the matching lower order.

The two representations are mathematical descriptions of the same unobserved noise. No localization outcomes or phase-flip records are supplied to a controller.

## Scope of optimality

The lower bound compares protocols built from quadratic coherent dynamics, classical randomization over such dynamics, and the same single vacuum-loss port. The chosen static uniform device attains that order. The earlier [Fermionic Reset Complexity](https://github.com/GoGoKo699/Fermionic-Reset-Complexity/tree/7cc91ccf5f1e7b503a95105b6d0b6885e1088349) result already permits interacting control to remove the logarithmic loss-action overhead. Here the scientific addition is a local autonomous realization of the noninteracting optimum.

The model has a known clean hopping chain and independent Markovian phase baths. Disorder, finite-temperature injection and the thermodynamic cost of creating the baths require separate analysis.
