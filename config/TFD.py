from config import creatLeftHamiltonian
import numpy as np
import qutip as qt


def termo_field_double(hamiltonian_left, beta=1.0):
    # Get eigenvalues and eigenvectors of H_L
    eigenvalues, eigenvectors = hamiltonian_left.eigenstates()

    # Calculate partition function
    Z = sum([np.exp(-beta * e) for e in eigenvalues])

    # Create the thermofield double state
    psi = sum([np.exp(-beta * e / 2) * qt.tensor(v, v.conj())
               for e, v in zip(eigenvalues, eigenvectors)])

    # Normalize the state
    return (1 / np.sqrt(Z)) * psi.unit()

