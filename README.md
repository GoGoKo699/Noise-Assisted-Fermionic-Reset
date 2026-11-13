# Noise Assisted Fermionic Reset

**Can weak phase noise make a simple quantum chain erase every input quickly?** A uniform fermion chain with one boundary loss port can retain coherent information for cubic time in its length. Adding independent, unobserved onsite dephasing at an inverse-length rate makes complete reset take order $`N\log N`$ at fixed global accuracy.

For $`N`$ modes, unit nearest-neighbor hopping, unit vacuum loss at one endpoint, and onsite dephasing rate $`\gamma=b/N`$ with fixed $`b>0`$, the optimal reset time of this fixed device is

```math
\boxed{\displaystyle
t_{N,b}(\epsilon)=\Theta_b\!\left(N\log\frac{N}{\epsilon}\right),
\qquad N\ge1,\quad 0<\epsilon\le\frac12.}
```

Error is half the diamond distance from global vacuum replacement. The guarantee covers arbitrary many-body inputs and arbitrary external references. The constants are uniform when $`b`$ varies over a fixed positive compact interval.

| Result | Meaning | Proof |
|---|---|---|
| Weak-noise complete reset: $`\Theta_b(N\log(N/\epsilon))`$ | Static local dynamics erase the whole register and its reference correlations. | [Reset theorem](science/reset_theorem.md) |
| Identical coherent chain: $`\Omega(N^3\log(1/\epsilon))`$ | A band-edge mode makes the native noiseless device slow in the worst case. | [Native comparison](science/native_comparator.md) |
| Any fixed rate window $`0<b_-\le b\le b_+<\infty`$ | Constant-factor rate error preserves the reset order. | [Uniform absorption](science/absorption.md) |

The logarithmic lower bound is inherited from the Gaussian loss-action frontier in [Fermionic Reset Complexity](https://github.com/GoGoKo699/Fermionic-Reset-Complexity/tree/7cc91ccf5f1e7b503a95105b6d0b6885e1088349). The contribution here is attaining that order autonomously with a uniform nearest-neighbor chain, one continuously active sink, and bounded total phase-noise strength. [Relationship to earlier work](references/RELATED_WORK.md)

## Why noise helps

Some coherent hopping modes have very little amplitude at the loss port. Independent phase noise breaks their protection. An exact endpoint resolvent gives a size-independent probability that a localized particle is absorbed before its next dephasing event. A regenerative estimate turns that probability into an $`O_b(N)`$ absorption scale for every coherent one-particle input. The closed occupation equation and a vacuum-projection bound then control the full quantum channel.

At $`b=1`$, one explicit pair of finite-size bounds is

```math
-N\log\!\left[1-(1-\epsilon)^{1/N}\right]
\le t_{N,1}(\epsilon)
\le192N\left\lceil\log_2\frac{4N}{\epsilon^2}\right\rceil.
```

The constants are deliberately conservative. The theorem identifies the scaling, without claiming an optimal finite-size prefactor or a cutoff profile.

## Read the science

Start with the [scientific overview](science/README.md), then follow the [model](science/model.md), [uniform absorption proof](science/absorption.md), and [complete reset theorem](science/reset_theorem.md). The [physical interpretation](science/interpretation.md) explains the resources, the role of independent noise, and the distinction between excitation transfer and erasing arbitrary quantum information. The [reference list](references/REFERENCES.md) identifies the primary precedents and pinned scientific accounts.

The [LLM reading guide](llms.txt) maps questions to authoritative files.

## Reproduce the finite checks

```bash
python -m pip install -r verification/requirements.txt
python verification/check_model.py
```

The [verification guide](verification/README.md) describes the tested domains and [saved results](verification/results.json). Checks compare full Fock evolution with a closed one-particle equation, include a reference-entangled non-Gaussian input, and verify the resolvent, absorption, phase-flip and slow-mode conventions. These finite diagnostics support the analytical account; they do not replace its arbitrary-size proofs.

## Scope

The hopping chain is clean and known; phase baths are independent and Markovian; the loss bath is ideal vacuum. The per-site noise rate is $`b/N`$, while the sum of dephasing coefficients is $`b`$. All loss and dephasing evolution enters the elapsed-time cost. There are no bath records, feedback, auxiliary register or active mode permutations.

Optimality is within the fixed noisy model and the corresponding randomized quadratic loss-action class. Interacting controls have a different reset frontier. The native coherent result is a cubic lower bound, not a claimed exact mixing law. Disorder, finite-temperature injection and bath-generation heat or work costs require separate analysis.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
