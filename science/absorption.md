# A uniform one-particle absorption bound

This page proves that weak number dephasing of rate $`\gamma=b/N`$ removes every one-particle state in mean time $`O_b(N)`$. The conclusion controls arbitrary coherent initial states, including the slow native modes. It is stronger than a statement about a localized initial particle or a spectral gap.

Let $`T_t`$ be the trace-decreasing CP semigroup on the one-particle space with generator

```math
\mathcal K(\rho)=-i[h_N,\rho]-\frac12\{P,\rho\}
 -\gamma(\rho-\mathrm{diag}\,\rho),
\qquad P=|1\rangle\langle1|,\quad \gamma=b/N.
```

Its trace is the probability that the particle has not been absorbed by the sink.

## Proposition

Define

```math
a_b=\frac{\sqrt3(\pi/6-1/4)}
 {2\pi e^{2b/\sqrt3}(3/2)^2},
\qquad
C_b=\frac{1+a_b^{-1}}{b}.
```

For every $`N\ge1`$ and every normalized initial one-particle density operator,

```math
\mathbb E_\rho\tau_{\rm abs}\le C_bN.
```

Consequently,

```math
\|T_t^*(I)\|_\infty
\le2^{-\lfloor t/(2C_bN)\rfloor}.
```

For $`b=1`$, the conservative constants satisfy $`a_1>0.01056409`$ and $`C_1\lt 95.661`$. A block length of $`192N`$ can therefore replace $`2C_1N`$. The constants are proof bounds, not optimized transport constants.

## Absorption before the next dephasing event

The projector-jump representation in the [model](model.md) gives a state-independent dephasing-event rate $`\gamma`$ until absorption. A dephasing event leaves the normalized state $`|j\rangle\langle j|`$ for some $`j`$.

Between these events, define the native killed propagator

```math
K_t=e^{(-ih_N-P/2)t}.
```

Starting at site $`j`$, the probability of sink absorption before the next dephasing event is

```math
p_j=\int_0^\infty e^{-\gamma t}|(K_t)_{1j}|^2\,dt.
```

The exponential factor is the probability of no dephasing event before time $`t`$; the remaining integrand is the unnormalized sink-absorption density. The aim is the uniform bound $`p_j\ge a_b`$.

## Endpoint Green function

Parseval's identity for the exponentially damped propagator gives

```math
p_j=\frac1{2\pi}\int_{\mathbb R}
 \left|\left[(E+i\gamma/2)I-h_N+iP/2\right]^{-1}_{1j}\right|^2dE.
```

All transforms are square integrable because $`\gamma>0`$. The possible overall phase from the Fourier-transform convention disappears inside the squared modulus.

The determinant recurrence of a path tridiagonal matrix gives

```math
\det(zI-h_N+iP/2)
=U_N(z/2)+(i/2)U_{N-1}(z/2),
```

where $`U_m`$ is the second-kind Chebyshev polynomial. The $`(1,j)`$ inverse entry has cofactor $`U_{N-j}(z/2)`$. If $`z=2\cos\theta`$, then

```math
G_{1j}(z)
=\frac{\sin[(N-j+1)\theta]}
 {\sin[(N+1)\theta]+(i/2)\sin(N\theta)}.
```

The formula is an identity of rational functions, with removable cases understood by continuity. On the integration contour $`\mathrm{Im}\,z=\gamma/2>0`$, the inverse exists because $`h_N-iP/2`$ is dissipative.

## A fixed energy band carries a uniform probability

Parameterize part of the integration contour by

```math
z=E+i\gamma/2=2\cos(x-iy),
\qquad \pi/3\le x\le2\pi/3,
```

```math
\sinh y=\frac{\gamma}{4\sin x}
=\frac b{4N\sin x},
\qquad E(x)=2\cos x\cosh y(x).
```

Then

```math
0\le y\le\frac b{2\sqrt3N},
\qquad (N+1)y\le\frac b{\sqrt3}.
```

Differentiation gives $`y'=-\cot x\tanh y`$ and

```math
-E'(x)=2\sin x\cosh y
 +\frac{2\cos^2x}{\sin x}\sinh y\tanh y
\ge\sqrt3.
```

Thus the real-energy parameterization is injective and its Jacobian is bounded below. Using $`|\sin(u+iv)|\le e^{|v|}`$, the denominator obeys

```math
|\sin[(N+1)\theta]+(i/2)\sin(N\theta)|^2
\le(3/2)^2e^{2b/\sqrt3}.
```

For $`m=N-j+1\ge1`$,

```math
|\sin[m(x-iy)]|^2
=\sin^2(mx)+\sinh^2(my)\ge\sin^2(mx).
```

The remaining elementary integral is uniformly positive:

```math
\begin{aligned}
\int_{\pi/3}^{2\pi/3}\sin^2(mx)dx
&=\frac\pi6-
 \frac{\sin(4\pi m/3)-\sin(2\pi m/3)}{4m}\\
&\ge\frac\pi6-\frac14.
\end{aligned}
```

For $`m\ge2`$ use the sine difference bound $`2`$ and $`1/(2m)\le1/4`$. For $`m=1`$ the integral is $`\pi/6+\sqrt3/4`$, so the same lower bound holds. Restricting Parseval's integral to this band now proves

```math
p_j\ge
\frac{\sqrt3(\pi/6-1/4)}
 {2\pi e^{2b/\sqrt3}(3/2)^2}=a_b
```

for every site and length.

## Renewal from arbitrary initial states

Divide a trajectory into intervals ending at either a dephasing event or sink absorption. Every interval, including the first interval from an arbitrary coherent state, has conditional mean length at most $`1/\gamma=N/b`$. Indeed, the probability an interval lasts beyond $`s`$ is at most $`e^{-\gamma s}`$, because it must contain no dephasing event and no absorption.

If the first interval ends with dephasing, its endpoint is a site state. Every subsequent interval then has conditional probability at least $`a_b`$ to end with absorption. The site labels need not be independent. The probability that $`k`$ subsequent intervals all end without absorption is at most $`(1-a_b)^k`$ by conditional iteration. Thus their expected number is at most $`1/a_b`$.

Summing conditional mean lengths gives

```math
\mathbb E_\rho\tau_{\rm abs}
\le\frac Nb\left(1+\frac1{a_b}\right)=C_bN.
```

One may first stop after a finite number of intervals, apply this bound, and pass to the limit by monotone convergence. The geometric tail also shows absorption occurs almost surely.

Markov's inequality gives survival probability at most $`1/2`$ after $`2C_bN`$. This bound applies to every normalized state. At any subsequent block boundary the normalized surviving state can therefore be used as a new initial state, giving

```math
\mathrm{Tr}\,T_t(\rho)
\le2^{-\lfloor t/(2C_bN)\rfloor}\mathrm{Tr}\,\rho
```

for positive $`\rho`$. By duality this is the stated operator bound. No conversion from a spectral gap to a mixing time, no eigenvector conditioning assumption, and no Gaussian-input assumption is needed.
