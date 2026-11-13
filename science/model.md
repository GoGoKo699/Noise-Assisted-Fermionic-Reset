# Uniform chain, one loss port, and complete reset

The task is to erase an entire quantum register, including its correlations with an arbitrary reference. A small density of residual particles is insufficient: the final register must be close to its global vacuum.

## Register and fixed generator

There are $`N\ge1`$ fermionic modes with canonical anticommutation relations

```math
\{c_i,c_j^\dagger\}=\delta_{ij}I,\qquad
\{c_i,c_j\}=0,\qquad n_j=c_j^\dagger c_j.
```

Fix the occupation ordering and use the ordinary matrix algebra on $`\mathcal H_N\cong\mathbb C^{2^N}`$. Set $`\hbar=1`$, hopping strength $`J=1`$, and loss strength $`\kappa=1`$. The Hamiltonian and master equation are

```math
H_N=\sum_{j=1}^{N-1}
 (c_j^\dagger c_{j+1}+c_{j+1}^\dagger c_j),
```

```math
\mathcal L_{N,b}(\rho)
=-i[H_N,\rho]+\mathcal D[c_1](\rho)
 +\frac bN\sum_{j=1}^N\mathcal D[n_j](\rho),
\qquad b>0,
```

```math
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

The main example is $`b=1`$. More generally, $`b`$ is any fixed positive constant independent of $`N`$. The [absorption proof](absorption.md) and [reset theorem](reset_theorem.md) give constants depending on $`b`$, uniformly when $`b`$ lies in a fixed compact subinterval of $`(0,\infty)`$.

All terms are time independent. The single loss port is an ideal Markovian vacuum bath at the first site. Number dephasing conserves total particle number. The bath outputs and all possible bath records are inaccessible. No feedback, postselection, auxiliary register, extra loss port, or time-dependent routing is supplied.

Under the open-chain Jordan–Wigner transformation this is also a local spin chain:

```math
H_N=\frac12\sum_{j=1}^{N-1}(X_jX_{j+1}+Y_jY_{j+1}),
\qquad c_1=|0\rangle\langle1|_1
=\frac{X_1+iY_1}{2},\qquad n_j=\frac{I-Z_j}{2}.
```

The bond strength, loss strength, and total dephasing coefficient are bounded independently of length. Specifically, the sum of the coefficients of $`\mathcal D[n_j]`$ is $`b`$, while each coefficient is $`b/N`$. The single-particle Hamiltonian has norm below $`2`$.

## Error and elapsed time

Write $`\Phi_{N,b,t}=e^{t\mathcal L_{N,b}}`$ and $`|\Omega_N\rangle=|0\rangle^{\otimes N}`$. The replacement channel and reset error are

```math
\mathcal R_N(X)=\operatorname{Tr}(X)
 |\Omega_N\rangle\langle\Omega_N|,
```

```math
\begin{aligned}
d_{N,b}(t)
&=\frac12\|\Phi_{N,b,t}-\mathcal R_N\|_\diamond\\
&=\sup_{\rho_{SR}}\frac12\left\|
 (\Phi_{N,b,t}\otimes\operatorname{id}_R)(\rho_{SR})
 -|\Omega_N\rangle\langle\Omega_N|\otimes\rho_R
 \right\|_1.
\end{aligned}
```

The supremum is over arbitrary states and references; a reference of dimension $`2^N`$ suffices. This is the ordinary diamond norm on the specified full matrix algebra. It includes parity-compatible fermionic tests and is also a direct spin-channel guarantee. No restriction to Gaussian inputs, product states, or a particle-number sector enters the reset theorem.

Define

```math
t_{N,b}(\epsilon)=\inf\{t\ge0:d_{N,b}(t)\le\epsilon\}.
```

The vacuum is stationary. Complete positivity and trace-norm contraction imply that $`d_{N,b}(t)`$ is nonincreasing. The theorem concerns elapsed physical time under this fixed generator, in the units above.

The sink action is exactly $`A=t`$. The dephasing exposure is also explicit: the sum of its coefficients integrated to time $`t`$ is $`bt`$. No thermodynamic work or heat advantage is claimed. Although number dephasing preserves particle number, it does not commute with $`H_N`$ and can exchange energy with the chain.

## One-body equation without a Gaussian-input assumption

For an arbitrary many-body input define

```math
C_{ij}(t)=\operatorname{Tr}
 \bigl[\Phi_{N,b,t}(\rho)c_j^\dagger c_i\bigr].
```

Let $`h_N`$ be the path adjacency matrix and $`P=|1\rangle\langle1|`$. Directly applying the adjoint generator to quadratic observables gives

```math
\dot C=-i[h_N,C]-\frac12\{P,C\}
 -\gamma(C-\operatorname{diag}C),\qquad \gamma=\frac bN.
```

For example,

```math
\mathcal D[n_j]^*(c_\ell^\dagger c_k)
=-\frac12(\delta_{jk}-\delta_{j\ell})^2c_\ell^\dagger c_k.
```

Summing over $`j`$ multiplies off-diagonal entries by $`-1`$ and leaves diagonal entries unchanged. The hopping and loss terms give the commutator and anticommutator above.

The CAR imply $`0\preceq C(0)\preceq I`$ and $`\operatorname{Tr}C(0)\le N`$. Also

```math
\operatorname{Tr}C(t)
=\operatorname{Tr}\bigl[\Phi_{N,b,t}(\rho)\widehat N\bigr],
\qquad \widehat N=\sum_j n_j.
```

The closed equation is valid even when the many-body state is not Gaussian. The proof uses this closure to control expected particle number, then a separate channel-norm argument to control every reference.

## Two exact representations of dephasing

The proofs use different representations of the same generator.

1. On the one-particle sector, the jumps $`\sqrt\gamma\,|j\rangle\langle j|`$ have total squared effect $`\gamma I`$. A dephasing event therefore occurs at constant rate $`\gamma`$ while the particle survives and localizes it to one site. This is the regenerative representation used in [absorption](absorption.md).
2. On the full register, put $`Z_j=I-2n_j=e^{i\pi n_j}`$. The exact identity

```math
\gamma\mathcal D[n_j]
=\frac\gamma4\mathcal D[Z_j]
=\frac\gamma4(Z_j\rho Z_j-\rho)
```

means that independent Poisson phase flips of rate $`\gamma/4`$ at each site reproduce the dephasing exactly. The total phase-flip rate is $`b/4`$. Each realization is a finite sequence of Gaussian, number-conserving unitary kicks between intervals of vacuum attenuation. This representation is used for the [determinant lower bound](reset_theorem.md#lower-bound-the-single-port-determinant-barrier).

These representations are proof devices. Their labels are not accessible control resources, and no conditioning or record-dependent operation is added to the physical channel.
