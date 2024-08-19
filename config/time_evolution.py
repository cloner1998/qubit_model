import scipy.sparse as sparse
from scipy.sparse.linalg import expm_multiply
import numpy as np
import qutip as qt


def time_evolution(psi, hamiltonian, t):
    # Time evolution operator
    time_evolution_operator = (-1j * hamiltonian * t).expm()
    return time_evolution_operator * psi
