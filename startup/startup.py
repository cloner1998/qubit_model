import numpy as np
import qutip as qt
from config import creatLeftHamiltonian, TFD, spins_spin_correlation, mutual_information, perturbation_function, \
    time_evolution
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# make hamiltonian : H_l×I + I×H_l
# not bad in performance
qubits = 6
left_hamiltonian = creatLeftHamiltonian.create_left_hamiltonian(qubits)
identity = qt.qeye([2] * qubits)
hamiltonian = qt.tensor(left_hamiltonian, identity) + qt.tensor(identity, left_hamiltonian)

# make TFD
# not bad in performance
psi_0 = TFD.termo_field_double(left_hamiltonian, beta=1.0)

# define perturbation
# not bad in performance
perturbation = perturbation_function.perturbation_function(qubits)

# time evolution
t_list = np.linspace(start=1, stop=10, num=10)
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
        print(mutual_information.mutual_information(density_matrix, qubits))
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
        print(spins_spin_correlation.spin_spin_correlation(psi_t, qubits))
        spins_spin_correlation_list.append(spins_spin_correlation.spin_spin_correlation(psi_t, qubits))
    return spins_spin_correlation_list


ss_list = spin_spin_info_list()


def spin_spin_correlation_plot():
    plt.figure(figsize=(10, 6))
    plt.plot(ss_list, label='Spin-Spin Correlation')
    plt.xlabel('tw')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Spin-Spin Correlation vs tw')
    plt.show()


m_list = mutual_info_list()


def mutual_information_plot():
    plt.figure(figsize=(10.0, 6.0))
    plt.plot(m_list, label='Mutual Information')
    plt.xlabel('tw')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Mutual Information vs tw')
    plt.show()
