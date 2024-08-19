from config import creatLeftHamiltonian
import numpy as np
import qutip as qt


def thermo_field_double(hamiltonian_left, beta=1.0):
    # Get eigenvalues and eigenvectors of H_L
    eigenvalues, eigenvectors = hamiltonian_left.eigenstates()

    # Calculate partition function
    exp_const = -beta
    partition_function_terms_vector = np.exp(exp_const * eigenvalues)
    Z = np.sum(partition_function_terms_vector)

    # Create the thermofield double state
    exp_const_2 = exp_const/2.0
    psi = np.sum([np.exp(exp_const_2 * e) * qt.tensor(v, v.conj())
               for e, v in zip(eigenvalues, eigenvectors)])

    # Normalize the state
    return (1 / np.sqrt(Z)) * psi.unit()
