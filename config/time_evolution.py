import scipy.sparse as sparse
from scipy.sparse.linalg import expm_multiply
import numpy as np


def time_evolution(psi, hamiltonian, t):
    # Time evolution operator
    hamiltonian_1 = np.array(hamiltonian, dtype=np.float64)
    hamiltonian_sparse = sparse.csr_matrix(hamiltonian_1)
    return expm_multiply((-1j * t) * hamiltonian_sparse, psi)
