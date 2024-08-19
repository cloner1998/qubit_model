import numpy as np
import qutip as qt
from config import creatLeftHamiltonian, TFD, spins_spin_correlation, mutual_information, perturbation_function, \
    time_evolution

# make hamiltonian : H_l×I + I×H_l
qubits = 10
left_hamiltonian = creatLeftHamiltonian.create_left_hamiltonian(qubits)
hamiltonian = qt.tensor(left_hamiltonian, qt.qeye(2 ** qubits)) + qt.tensor(qt.qeye(2 ** qubits), left_hamiltonian)

# make TFD
psi_0 = TFD.termo_field_double(left_hamiltonian, beta=1.0)

# define perturbation
perturbation = perturbation_function.perturbation_function(qubits)

# time evolution
t_list = np.linspace(1, 10, 100)
mutual_information_list = []
spins_spin_correlation_list = []


def mutual_info_list():
    for t in t_list:
        # Apply perturbation in the past
        psi_t = time_evolution.time_evolution(psi_0, hamiltonian, -t)
        psi_t = perturbation * psi_t

        # Evolve forward
        psi_t = time_evolution.time_evolution(psi_t, hamiltonian, t)

        # Compute observables
        density_matrix = psi_t * psi_t.dag()
        mutual_information_list.append(mutual_information.mutual_information(density_matrix, qubits))
    return mutual_information_list


def spin_spin_info_list():
    for t in t_list:
        # Apply perturbation in the past
        psi_t = time_evolution.time_evolution(psi_0, hamiltonian, -t)
        psi_t = perturbation * psi_t

        # Evolve forward
        psi_t = time_evolution.time_evolution(psi_t, hamiltonian, t)

        # Compute observables
        spins_spin_correlation_list.append(spins_spin_correlation.spin_spin_correlation(psi_t, qubits))
    return spins_spin_correlation_list
