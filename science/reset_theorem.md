# Optimal reset order for the fixed noisy chain

For the [model](model.md) with any fixed $`b>0`$, let $`t_{N,b}(\epsilon)`$ be the elapsed time needed for half-diamond error $`\epsilon`$ from global vacuum replacement.

## Theorem

For all $`N\ge1`$ and $`0\lt \epsilon\le1/2`$,

```math
t_{N,b}(\epsilon)
=\Theta_b\!\left(N\log\frac N\epsilon\right).
```

The constants are uniform for $`b`$ in a fixed compact subinterval of $`(0,\infty)`$. For example, with $`C_b`$ defined in [absorption](absorption.md),

```math
\begin{aligned}
-N\log\left[1-(1-\epsilon)^{1/N}\right]
&\le t_{N,b}(\epsilon)\\
&\le2C_bN\left\lceil
 \log_2\frac{4N}{\epsilon^2}\right\rceil.
\end{aligned}
```

At $`b=1`$ the upper prefactor $`2C_1`$ can be replaced by $`192`$. These constants do not specify an optimal leading coefficient or a cutoff profile.

The result attains the single-port Gaussian loss-action order with a static nearest-neighbor Hamiltonian and weak local noise. Its optimality is within the stated fixed model, and the fully occupied lower-bound witness also constrains prescribed number-conserving quadratic controls with random Gaussian phase kicks and the same loss action. It is not an optimum over arbitrary interacting erasure machines.

## Upper bound: from one-particle survival to every reference

Let $`C(t)`$ be the covariance matrix of an arbitrary many-body input, as in the [model](model.md). It obeys $`C(t)=T_t(C(0))`$, with $`0\preceq C(0)\preceq I`$. Put

```math
q_b(t)=2^{-\lfloor t/(2C_bN)\rfloor},
\qquad \delta_t=Nq_b(t).
```

The [absorption proposition](absorption.md) implies

```math
\begin{aligned}
\operatorname{Tr}C(t)
&=\operatorname{Tr}\bigl[C(0)T_t^*(I)\bigr]\\
&\le q_b(t)\operatorname{Tr}C(0)\le\delta_t.
\end{aligned}
```

The number operator satisfies

```math
I-|\Omega_N\rangle\langle\Omega_N|\preceq\widehat N.
```

Hence every input has probability at most $`\delta_t`$ to be outside the vacuum after time $`t`$. The same statement applies to the system marginal of an input entangled with any reference.

To turn this into a channel bound, take an arbitrary output state $`\omega_{SR}`$ and set $`P_0=|\Omega_N\rangle\langle\Omega_N|\otimes I_R`$. If the nonvacuum probability is at most $`\delta\le1`$, gentle projection gives

```math
\|\omega-P_0\omega P_0\|_1\le2\sqrt\delta.
```

Write $`P_0\omega P_0=|\Omega_N\rangle\langle\Omega_N|\otimes\omega_R^0`$. Partial trace over the system kills the off-diagonal vacuum/nonvacuum blocks. Therefore $`\omega_R-\omega_R^0`$ is positive with trace at most $`\delta`$. Trace preservation gives $`\omega_R=\rho_R`$, the original reference marginal. The triangle inequality yields

```math
\frac12\left\|\omega_{SR}
 -|\Omega_N\rangle\langle\Omega_N|\otimes\rho_R\right\|_1
\le\sqrt\delta+\frac\delta2.
```

This holds uniformly over all input states and all references. Thus, whenever $`\delta_t\le1`$,

```math
d_{N,b}(t)\le\sqrt{\delta_t}+\frac{\delta_t}{2}.
```

Choosing $`\delta_t\le\epsilon^2/4`$ proves the stated upper bound. The complete-channel guarantee follows from expected total occupation and the reference argument together; an occupation estimate alone would not establish diamond-norm reset.

## Lower bound: the single-port determinant barrier

The logarithmic Gaussian action obstruction is inherited from [Fermionic-Reset-Complexity, Gaussian bound, Sections 5–8, revision 7cc91cc](https://github.com/GoGoKo699/Fermionic-Reset-Complexity/blob/7cc91ccf5f1e7b503a95105b6d0b6885e1088349/science/gaussian_bound.md). That account permits arbitrary prescribed quadratic controls, Gaussian pulses, and classical randomization with a branchwise loss-action bound. It uses a maximally mixed input and proves the sharp witness frontier $`(1-e^{-A/N}/2)^N`$. The proof below is the number-conserving specialization of that determinant mechanism; the fully occupied witness is a routine finite-time sharpening, rather than an independent contribution.

For the present number-conserving model, a fully occupied input gives the following direct, slightly sharper finite-time witness. The argument is included to specify exactly why the obstruction still applies to dephasing, whose averaged dynamics need not preserve Gaussian states.

Use the exact Poisson phase-flip representation

```math
\frac bN\mathcal D[n_j]
=\frac b{4N}(Z_j\rho Z_j-\rho),
\qquad Z_j=e^{i\pi n_j}.
```

At every finite time there are almost surely finitely many flips. Conditional on their times and labels, the channel is a sequence of prescribed Gaussian unitaries interleaved with the same vacuum-loss channel. Each branch has sink action exactly $`t`$. This exact finite-rate representation makes the trajectorywise Gaussian argument applicable even when the averaged state is non-Gaussian.

Let $`K_\omega(t)`$ be a branch's one-particle attenuation matrix. Between flips,

```math
\dot K=(-ih_N-P/2)K.
```

At a phase flip it is left-multiplied by $`I-2|j\rangle\langle j|`$, a unitary matrix of determinant modulus one. Liouville's determinant formula therefore gives, branchwise,

```math
\det\bigl(K_\omega(t)^\dagger K_\omega(t)\bigr)=e^{-t}.
```

The propagator is contractive, so its squared singular values satisfy $`0\lt s_i\le1`$. Starting from the fully occupied Slater state, a branch is a gauge-invariant fermionic Gaussian attenuation state with covariance $`K_\omega K_\omega^\dagger`$. Its vacuum probability is

```math
P_{\rm vac}(t\mid\omega)=\prod_{i=1}^N(1-s_i),
\qquad\prod_{i=1}^N s_i=e^{-t}.
```

This Gaussian normal-form fact concerns each branch only. It can also be obtained by diagonalizing the attenuation matrix into independent lossy modes; a fully occupied input is invariant, up to phase, under number-conserving mode rotations.

For $`x\lt 0`$, $`f(x)=\log(1-e^x)`$ is concave. Applying Jensen's inequality to $`x_i=\log s_i`$ gives

```math
P_{\rm vac}(t\mid\omega)
\le\left(1-e^{-t/N}\right)^N.
```

If some $`s_i=1`$, the left side is zero and the same bound follows by continuity. Vacuum probability is linear in the state, so averaging over the Poisson branches preserves this inequality. A vacuum/nonvacuum measurement on the fully occupied test input gives

```math
d_{N,b}(t)\ge
1-\left(1-e^{-t/N}\right)^N.
```

It follows that $`d_{N,b}(t)\le\epsilon`$ requires

```math
t\ge-N\log\left[1-(1-\epsilon)^{1/N}\right].
```

This converse uses one allowed input and no reference, which suffices to lower-bound the supremum defining the diamond norm.

## Uniform order and the positive rate window

Let $`\alpha=-\log(1-\epsilon)`$. Since $`1-e^{-\alpha/N}\le\alpha/N`$,

```math
-N\log\left[1-(1-\epsilon)^{1/N}\right]
\ge N\log\frac N\alpha.
```

For $`0\lt \epsilon\le1/2`$, one has $`\alpha\le2(\log2)\epsilon`$. Also $`N/\epsilon\ge2`$, so the subtraction of $`\log(2\log2)`$ can be absorbed in a universal positive multiple of $`\log(N/\epsilon)`$. This proves a uniform lower order $`\Omega[N\log(N/\epsilon)]`$. The explicit upper bound has the same order.

For $`b\in[b_-,b_+]\subset(0,\infty)`$, use

```math
a_b\ge a_{b_+},\qquad
C_b\le\frac{1+a_{b_+}^{-1}}{b_-}.
```

Hence the theorem holds uniformly throughout that rate window. It does not give uniform constants as $`b\to0`$ or $`b\to\infty`$, nor does it identify a unique optimal dephasing rate. At fixed $`\epsilon`$, the lower bound is $`N\log N+O_\epsilon(N)`$; the proof does not match its leading coefficient with the achievable upper bound.

## What changes compared with the native chain

The [native comparator](native_comparator.md) has exactly the same Hamiltonian and loss port and sets dephasing to zero. Its slow coherent mode forces reset time at least $`\Omega(N^3)`$ at fixed error. The weak noisy chain instead resets the entire register in $`O(N\log N)`$, while retaining the full input and reference guarantee. The comparison charges the added dephasing and restricts both sides to their stated fixed generators. Fast Gaussian mode routing and interacting erasure are different architectures.
