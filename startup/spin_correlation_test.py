import numpy as np
import qutip as qt


def create_propagator(hamiltonian, t):
    return (-1j * hamiltonian * t).expm()


def time_evolution_propagator(psi, propagator):
    return propagator * psi


def spin_spin_info_list(psi_0, hamiltonian, t_list, qubits, perturbation):
    print("Starting spin-spin correlation calculation")
    spins_spin_correlation_list = []

    for t in t_list:
        print(f"Time t = {t}")

        # Create propagators for backward and forward evolution
        U_backward = create_propagator(hamiltonian, -t)
        U_forward = create_propagator(hamiltonian, t)

        # Apply perturbation in the past
        psi_t = time_evolution_propagator(psi_0, U_backward)
        psi_t = perturbation * psi_t

        # Evolve forward
        psi_t = time_evolution_propagator(psi_t, U_forward)

        # Compute observables
        correlation = spins_spin_correlation(psi_t, qubits)
        print(f"Spin-spin correlation: {correlation}")
        spins_spin_correlation_list.append(correlation)

    return spins_spin_correlation_list


def spins_spin_correlation(psi, qubits):
    # Assuming this function is defined elsewhere
    # If not, you should implement it here

    op = qt.tensor([qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1) + [qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1))
    print("op")
    print(op)
    print("psi")
    print(psi)
    return qt.expect(op, psi)

