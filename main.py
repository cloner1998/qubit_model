from config import creatLeftHamiltonian, TFD, time_evolution
from startup import init, test
import qutip as qt
import numpy as np
from startup.spin_correlation_test import spin_spin_info_list
from startup.init import identity, hamiltonian, psi_0, t_list, perturbation

if __name__ == '__main__':
    t_list = np.linspace(0, 10, 100)  # or whatever time range you're using
    qubits = 6  # or however many qubits you're using
    spin_spin_info_list(psi_0=psi_0, hamiltonian=hamiltonian, qubits=qubits, perturbation=perturbation, t_list=t_list)

