#!/usr/bin/env python3
"""Deterministic finite diagnostics for noise-assisted fermionic reset.

These checks compare independently formulated representations of the model.
They are floating-point diagnostics, not interval certificates or proofs of
arbitrary-size scaling.  Run: python verification/check_model.py
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import time
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import eigvals, expm, solve_continuous_lyapunov
from scipy.sparse import csr_matrix, diags, eye, kron
from scipy.sparse.linalg import expm_multiply


def fock_operators(n: int) -> list[np.ndarray]:
    """Jordan-Wigner annihilators; |0> is empty and site 0 is leftmost."""
    lower = np.array([[0.0, 1.0], [0.0, 0.0]], complex)
    z = np.diag([1.0, -1.0])
    ident = np.eye(2)
    out = []
    for j in range(n):
        value = np.ones((1, 1), complex)
        for k in range(n):
            value = np.kron(value, z if k < j else lower if k == j else ident)
        out.append(value)
    return out


def gksl(hamiltonian: np.ndarray, jumps: list[np.ndarray]) -> csr_matrix:
    """Full Fock GKSL generator, using column-major vectorization."""
    d = len(hamiltonian)
    ident = eye(d, format="csr", dtype=complex)
    h = csr_matrix(hamiltonian)
    result = -1j * (kron(ident, h) - kron(h.T, ident))
    for jump in jumps:
        op = csr_matrix(jump)
        rate = op.conj().T @ op
        result += kron(op.conj(), op) - 0.5 * (
            kron(ident, rate) + kron(rate.T, ident)
        )
    return result.tocsr()


def evolve(generator: csr_matrix, rho: np.ndarray, duration: float) -> np.ndarray:
    vector = expm_multiply(
        generator * duration,
        rho.reshape(-1, order="F"),
        traceA=duration * generator.diagonal().sum(),
    )
    return vector.reshape(rho.shape, order="F")


def one_particle(n: int, gamma: float, kappa: float = 1.0):
    h = diags([np.ones(n - 1), np.ones(n - 1)], [-1, 1], shape=(n, n), format="csr")
    ident = eye(n, format="csr", dtype=complex)
    port = diags([1.0] + [0.0] * (n - 1), format="csr")
    diagonal = np.zeros(n * n)
    diagonal[np.arange(n) * (n + 1)] = 1.0
    generator = (
        -1j * (kron(ident, h) - kron(h.T, ident))
        - (kappa / 2) * (kron(ident, port) + kron(port, ident))
        - gamma * diags(1.0 - diagonal)
    ).tocsr()
    return h.toarray(), port.toarray(), generator


def onebody(rho: np.ndarray, annihilators: list[np.ndarray]) -> np.ndarray:
    return np.array([
        [np.trace(rho @ (ck.conj().T @ cj)) for ck in annihilators]
        for cj in annihilators
    ])


def half_trace_norm(hermitian: np.ndarray) -> float:
    return float(np.abs(np.linalg.eigvalsh((hermitian + hermitian.conj().T) / 2)).sum() / 2)


def check_fock_and_reference():
    rows = []
    for n in (2, 3, 4):
        annihilators = fock_operators(n)
        d = 2**n
        ident = np.eye(d)
        occupations = [c.conj().T @ c for c in annihilators]
        h = sum(
            annihilators[j].conj().T @ annihilators[j + 1]
            + annihilators[j + 1].conj().T @ annihilators[j]
            for j in range(n - 1)
        )
        gamma = 1 / n
        jumps = [annihilators[0]] + [math.sqrt(gamma) * op for op in occupations]
        generator = gksl(h, jumps)
        car_error = max(
            float(np.max(np.abs(
                annihilators[j] @ annihilators[k].conj().T
                + annihilators[k].conj().T @ annihilators[j]
                - (ident if j == k else 0)
            )))
            for j in range(n) for k in range(n)
        )
        # Both system branches have even parity.  The system's reduced input
        # violates Wick factorization and is not assumed Gaussian.
        pattern = d - 1 if n % 2 == 0 else 2 ** (n - 1) + 2 ** (n - 2)
        psi = np.zeros(2 * d, complex)
        psi[0] = psi[2 * pattern + 1] = 1 / math.sqrt(2)
        rho_sr = np.outer(psi, psi.conj())
        rho_s = np.trace(rho_sr.reshape(d, 2, d, 2), axis1=1, axis2=3)
        rho_r = np.trace(rho_sr.reshape(d, 2, d, 2), axis1=0, axis2=2)
        g0 = onebody(rho_s, annihilators)
        wick_defect = float(abs(
            np.trace(rho_s @ occupations[0] @ occupations[1])
            - g0[0, 0] * g0[1, 1] + g0[0, 1] * g0[1, 0]
            - abs(np.trace(rho_s @ annihilators[0] @ annihilators[1]))**2
        ))
        ref_generator = gksl(
            np.kron(h, np.eye(2)), [np.kron(op, np.eye(2)) for op in jumps]
        )
        _, _, small_generator = one_particle(n, gamma)
        vacuum = np.zeros((d, d), complex)
        vacuum[0, 0] = 1
        for duration in (0.37 * n, 2.0 * n):
            output = evolve(ref_generator, rho_sr, duration)
            reduced = np.trace(output.reshape(d, 2, d, 2), axis1=1, axis2=3)
            output_ref = np.trace(output.reshape(d, 2, d, 2), axis1=0, axis2=2)
            exact_g = onebody(reduced, annihilators)
            predicted_g = evolve(small_generator, g0, duration)
            closure_error = float(np.max(np.abs(exact_g - predicted_g)))
            reference_error = float(np.max(np.abs(output_ref - rho_r)))
            nonvacuum = max(0.0, float(1 - reduced[0, 0].real))
            mean_number = max(0.0, float(np.trace(exact_g).real))
            distance = half_trace_norm(output - np.kron(vacuum, rho_r))
            gentle_bound = math.sqrt(nonvacuum) + nonvacuum / 2
            assert closure_error < 2e-11
            assert reference_error < 2e-11
            assert nonvacuum <= mean_number + 2e-11
            assert distance <= gentle_bound + 2e-11
            assert car_error < 1e-13 and wick_defect > 0.2
            rows.append({
                "n": n, "time": duration, "input_reference_ebits": 1,
                "initial_wick_defect": wick_defect, "jw_car_error": car_error,
                "onebody_closure_max_error": closure_error,
                "reference_marginal_max_error": reference_error,
                "nonvacuum_probability": nonvacuum,
                "mean_particle_number": mean_number,
                "half_trace_distance_to_vacuum_replacement": distance,
                "gentle_projection_bound_using_actual_nonvacuum": gentle_bound,
                "trace_error": float(abs(np.trace(output) - 1)),
            })
        # Projector dephasing is EXACTLY a random Gaussian parity-kick generator.
        alternate = gksl(h, [annihilators[0]])
        super_ident = eye(d * d, format="csr", dtype=complex)
        for number in occupations:
            parity = csr_matrix(ident - 2 * number)
            alternate += (gamma / 4) * (kron(parity.conj(), parity) - super_ident)
        difference = generator - alternate
        parity_error = float(np.max(np.abs(difference.data))) if difference.nnz else 0.0
        assert parity_error < 1e-13
        rows.append({"n": n, "exact_parity_kick_generator_max_error": parity_error})
    return rows


def chebyshev_resolvent(n: int, j: int, z: complex, kappa: float = 1.0) -> complex:
    theta = np.arccos(complex(z) / 2)
    return np.sin((n - j) * theta) / (
        np.sin((n + 1) * theta) + 1j * kappa / 2 * np.sin(n * theta)
    )


def lower_absorption_constant(b: float, kappa: float = 1.0) -> float:
    return (
        kappa * math.sqrt(3) * (math.pi / 6 - 1 / 4)
        / (2 * math.pi * math.exp(2 * b / math.sqrt(3)) * (1 + kappa / 2)**2)
    )


def check_absorption_and_resolvent():
    rows = []
    for n in (2, 4, 8, 16, 32, 64):
        for b in (0.5, 1.0, 2.0):
            gamma = b / n
            h, port, _ = one_particle(n, gamma)
            killed = -1j * h - port / 2 - gamma * np.eye(n) / 2
            absorption = solve_continuous_lyapunov(killed.conj().T, -port)
            segment_time = solve_continuous_lyapunov(killed.conj().T, -np.eye(n))
            probabilities = np.diag(absorption).real
            conservation = float(np.max(np.abs(absorption + gamma * segment_time - np.eye(n))))
            formula_error = 0.0
            for energy in (-2.7, -1.3, 0.27, 1.1, 2.6):
                z = energy + 1j * gamma / 2
                inverse = np.linalg.inv(z * np.eye(n) - h + 1j * port / 2)
                for j in (0, n // 2, n - 1):
                    formula_error = max(formula_error, abs(
                        inverse[0, j] - chebyshev_resolvent(n, j, z)
                    ))
            analytic_lower = lower_absorption_constant(b)
            assert float(probabilities.min()) >= analytic_lower - 1e-10
            assert conservation < 2e-10
            assert formula_error < 2e-10
            row = {
                "n": n, "b": b, "gamma": gamma,
                "minimum_site_absorption_before_dephasing": float(probabilities.min()),
                "maximum_site_absorption_before_dephasing": float(probabilities.max()),
                "analytic_uniform_lower_bound": analytic_lower,
                "absorption_plus_dephasing_conservation_error": conservation,
                "chebyshev_vs_dense_resolvent_max_error": float(formula_error),
                "maximum_mean_segment_duration": float(np.diag(segment_time).real.max()),
                "mean_segment_upper_bound": 1 / gamma,
            }
            if n == 8 and b == 1:
                comparisons = []
                for j in (0, n // 2, n - 1):
                    integral, quadrature_error = quad(
                        lambda energy: abs(chebyshev_resolvent(
                            n, j, energy + 1j * gamma / 2
                        ))**2 / (2 * math.pi),
                        -np.inf, np.inf, epsabs=2e-10, epsrel=2e-10, limit=250,
                    )
                    error = abs(integral - probabilities[j])
                    assert error < 2e-8
                    comparisons.append({
                        "site_1_based": j + 1, "resolvent_integral": integral,
                        "lyapunov_value": float(probabilities[j]),
                        "absolute_difference": float(error),
                        "quadrature_reported_error": quadrature_error,
                    })
                row["plancherel_integral_comparison"] = comparisons
            rows.append(row)
    return rows


def check_survival_window():
    rows = []
    for n in (8, 16, 32, 64):
        for b in (0.5, 1.0, 2.0):
            _, _, generator = one_particle(n, b / n)
            duration = 4 * n
            # The largest eigenvalue of the adjoint survival effect equals the
            # maximum survival probability over ALL coherent input states.
            effect = evolve(generator.conj().T.tocsr(), np.eye(n), duration)
            effect = (effect + effect.conj().T) / 2
            values = np.linalg.eigvalsh(effect)
            q = float(values.max())
            assert values.min() > -2e-10 and q < 1 + 2e-10
            assert q < 0.5  # Only the stated finite sample and t=4N are checked.
            rows.append({
                "n": n, "b": b, "time": duration,
                "all_input_survival_norm": q,
                "minimum_survival_effect_eigenvalue": float(values.min()),
                "mean_survival_effect_eigenvalue": float(values.mean()),
            })
    return rows


def check_gaussian_phase_kick_bound():
    rows = []
    for n in (2, 3, 4):
        annihilators = fock_operators(n)
        d = 2**n
        h = sum(
            annihilators[j].conj().T @ annihilators[j + 1]
            + annihilators[j + 1].conj().T @ annihilators[j]
            for j in range(n - 1)
        )
        h1, port, _ = one_particle(n, 0)
        killed = -1j * h1 - port / 2
        generator = gksl(h, [annihilators[0]])
        duration = 1.7 * n
        for branch in (0, 1):
            rho = np.eye(d, dtype=complex) / d
            rho_full = np.zeros((d, d), complex)
            rho_full[-1, -1] = 1
            transfer = np.eye(n, dtype=complex)
            last = 0.0
            for event, fraction in enumerate((0.13, 0.37, 0.61, 0.83, 1.0)):
                interval = duration * (fraction - last)
                rho = evolve(generator, rho, interval)
                rho_full = evolve(generator, rho_full, interval)
                transfer = expm(killed * interval) @ transfer
                if fraction < 1:
                    j = (2 * event + branch) % n
                    number = annihilators[j].conj().T @ annihilators[j]
                    phase_fock = np.eye(d) - 2 * number
                    rho = phase_fock @ rho @ phase_fock
                    rho_full = phase_fock @ rho_full @ phase_fock
                    phase_one = np.eye(n)
                    phase_one[j, j] = -1
                    transfer = phase_one @ transfer
                last = fraction
            survival = transfer @ transfer.conj().T
            predicted_vacuum = float(np.linalg.det(np.eye(n) - survival / 2).real)
            actual_vacuum = float(rho[0, 0].real)
            frontier = (1 - 0.5 * math.exp(-duration / n))**n
            predicted_full = float(np.linalg.det(np.eye(n) - survival).real)
            actual_full = float(rho_full[0, 0].real)
            frontier_full = (1 - math.exp(-duration / n))**n
            determinant_error = float(abs(np.linalg.det(survival) - math.exp(-duration)))
            assert abs(predicted_vacuum - actual_vacuum) < 2e-11
            assert actual_vacuum <= frontier + 2e-11
            assert abs(predicted_full - actual_full) < 2e-11
            assert actual_full <= frontier_full + 2e-11
            assert determinant_error < 2e-11
            rows.append({
                "n": n, "deterministic_phase_kick_branch": branch,
                "time_and_damping_action": duration,
                "full_fock_vacuum_probability": actual_vacuum,
                "passive_gaussian_determinant_probability": predicted_vacuum,
                "inherited_gaussian_frontier": frontier,
                "fully_occupied_fock_vacuum_probability": actual_full,
                "fully_occupied_determinant_probability": predicted_full,
                "fully_occupied_frontier": frontier_full,
                "fixed_action_survival_determinant_error": determinant_error,
            })
    return rows


def check_native_cubic_mode():
    rows = []
    predicted_limit = 2 * math.pi**2 / (1 + 1 / 4)
    for n in (16, 32, 64, 128):
        h, port, _ = one_particle(n, 0)
        frequencies = eigvals(h - 1j * port / 2)
        population_rate = float(np.min(-2 * frequencies.imag))
        scaled = population_rate * n**3
        rows.append({
            "n": n, "slowest_one_particle_population_decay_rate": population_rate,
            "rate_times_n_cubed": scaled,
            "predicted_asymptotic_constant": predicted_limit,
            "relative_difference_from_limit": abs(scaled / predicted_limit - 1),
        })
    assert rows[-1]["relative_difference_from_limit"] < 0.05
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    started = time.perf_counter()
    result = {
        "passed": True,
        "scope": (
            "Deterministic floating-point finite diagnostics. No interval certificate, "
            "arbitrary-size proof, priority certificate, or physical implementation validation. "
            "The t=4N finite survival values are not the conservative analytical block constant."
        ),
        "conventions": {
            "J": 1, "kappa": 1, "gamma": "b/N",
            "gksl": "D[L](rho)=L rho L^dagger-{L^dagger L,rho}/2",
            "jumps": "L0=c1; Lj=sqrt(gamma) n_j",
            "onebody": "G_jk=Tr(rho c_k^dagger c_j)",
            "error": "half trace/diamond distance; the script checks selected trace distances",
            "phase_kick_identity": "gamma D[n_j]=(gamma/4)(P_j rho P_j-rho), P_j=I-2n_j",
        },
        "runtime": {
            "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
        },
    }
    result["full_fock_reference_checks"] = check_fock_and_reference()
    result["resolvent_absorption_checks"] = check_absorption_and_resolvent()
    result["finite_rate_window_survival"] = check_survival_window()
    result["gaussian_phase_kick_branches"] = check_gaussian_phase_kick_bound()
    result["native_band_edge_mode"] = check_native_cubic_mode()
    result["runtime"]["elapsed_seconds"] = time.perf_counter() - started
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "passed": result["passed"], "output": str(args.output),
        "elapsed_seconds": result["runtime"]["elapsed_seconds"],
        "minimum_analytical_absorption_constant_at_b1": lower_absorption_constant(1),
        "largest_finite_survival_norm": max(x["all_input_survival_norm"] for x in result["finite_rate_window_survival"]),
        "largest_onebody_closure_error": max(x.get("onebody_closure_max_error", 0) for x in result["full_fock_reference_checks"]),
    }, indent=2))


if __name__ == "__main__":
    main()
