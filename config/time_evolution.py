import scipy.sparse as sparse
from scipy.sparse.linalg import expm_multiply
import numpy as np
import qutip as qt


def hamiltonian_convert_to_sparse(hamiltonian):
    # QuTiP objects are already stored in a sparse format internally
    return hamiltonian


def time_evolution(psi, hamiltonian, t):
    # Time evolution operator
    # Use QuTiP's sesolve for time evolution
    result = qt.sesolve(hamiltonian, psi, [t])
    return result.states[-1]
