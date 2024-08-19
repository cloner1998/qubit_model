from config import time_evolution
from startup.init import t_list, psi_0, hamiltonian, perturbation, spins_spin_correlation_list, qubits
import qutip as qt


def spin_spin_info_list():
    print("Starting spin-spin correlation calculation")
    for t in t_list:
        print(f"Time t = {t}")

        # Apply perturbation in the past
        psi_t = time_evolution.time_evolution(psi_0, hamiltonian, -t)
        print(f"State after backward evolution: {psi_t}")

        psi_t = perturbation * psi_t
        print(f"State after perturbation: {psi_t}")

        # Evolve forward
        psi_t = time_evolution.time_evolution(psi_t, hamiltonian, t)
        print(f"State after forward evolution: {psi_t}")

        # Compute observables
        op = qt.tensor([qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1) + [qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1))
        correlation = qt.expect(op, psi_t)
        print(f"Spin-spin correlation: {correlation}")
        spins_spin_correlation_list.append(correlation)

    return spins_spin_correlation_list
