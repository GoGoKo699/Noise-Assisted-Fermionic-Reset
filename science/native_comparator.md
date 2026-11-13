# A slow mode of the native chain

The native comparator has exactly the [same uniform Hamiltonian and boundary loss port](model.md), with every dephasing coefficient set to zero. It has no time-dependent controls or extra routing operations. This page proves the lower bound needed for the comparison:

```math
t_{N,0}(\epsilon)=\Omega\!\left(N^3\log\frac1\epsilon\right)
\qquad(0\lt \epsilon\le1/2).
```

In particular its fixed-error reset time is at least cubic, whereas the [weak noisy chain](reset_theorem.md) has order $`N\log N`$. A matching native cubic upper bound is not required by this statement and is not inferred from a spectral gap.

## Characteristic equation

In the one-particle sector the no-absorption propagator is

```math
K_t=e^{-ih_{\rm eff}t},\qquad
h_{\rm eff}=h_N-iP/2,
\qquad P=|1\rangle\langle1|.
```

The determinant recurrence used in [absorption](absorption.md) gives

```math
\det(zI-h_{\rm eff})
=U_N(z/2)+(i/2)U_{N-1}(z/2).
```

Putting $`z=2\cos\theta`$ therefore gives the eigenvalue equation

```math
\sin[(N+1)\theta]+(i/2)\sin(N\theta)=0,
```

provided $`\sin\theta\ne0`$. The root constructed below has this property for all sufficiently large $`N`$.

## A cubic decay rate by the implicit-function theorem

Set $`u=1/N`$ and $`\theta=uw`$. Consider the holomorphic function

```math
F(w,u)=\sin[(1+u)w]+(i/2)\sin w.
```

At $`(w,u)=(\pi,0)`$,

```math
F(\pi,0)=0,\qquad
\partial_wF(\pi,0)=-(1+i/2)\ne0.
```

There is therefore an analytic root branch with

```math
w(u)=\pi-\frac\pi{1+i/2}u+O(u^2)
=\pi-\frac{4\pi}{5}u+i\frac{2\pi}{5}u+O(u^2).
```

Expanding $`z_N=2\cos[uw(u)]`$ gives

```math
\mathrm{Im}\,z_N
=-\frac{4\pi^2}{5N^3}+O(N^{-4}),
```

and hence the survival-probability decay rate is

```math
r_N=-2\mathrm{Im}\,z_N
=\frac{8\pi^2}{5N^3}+O(N^{-4}).
```

This is a genuine eigenvalue, not a first-order perturbation estimate with an unexamined level-spacing assumption.

## The eigenvector is a valid reset test input

Let $`|v_N\rangle`$ be any normalized right eigenvector for $`z_N`$. Nonnormality causes no difficulty for this test because

```math
K_t|v_N\rangle=e^{-iz_Nt}|v_N\rangle
```

holds exactly. Starting in this one-particle state, the output under the full native loss channel is

```math
\Phi_{N,0,t}(|v_N\rangle\langle v_N|)
=e^{-r_Nt}|v_N\rangle\langle v_N|
 +(1-e^{-r_Nt})|\Omega_N\rangle\langle\Omega_N|.
```

Every sink jump removes the only particle, after which the vacuum is stationary. The trace distance from vacuum is exactly $`e^{-r_Nt}`$. Consequently

```math
d_{N,0}(t)\ge e^{-r_Nt},\qquad
t_{N,0}(\epsilon)\ge\frac{\log(1/\epsilon)}{r_N}.
```

Since $`r_N=\Theta(N^{-3})`$, this proves the cubic lower bound. Finitely many small lengths can be absorbed in its constant. Their decay rates are strictly positive: if a right eigenvector of $`h_N-iP/2`$ had a real eigenvalue, its imaginary expectation value would force its first component to vanish, and the path recurrence would then force every component to vanish.

The argument identifies a weakly visible band-edge mode. It does not claim that the same mode controls a sharp whole-channel mixing profile, nor that all noiseless reset architectures are cubic. In particular, externally controlled mode permutations belong to the broader Gaussian-control model of [Fermionic-Reset-Complexity](https://github.com/GoGoKo699/Fermionic-Reset-Complexity/blob/7cc91ccf5f1e7b503a95105b6d0b6885e1088349/science/model.md), rather than this fixed native chain.
