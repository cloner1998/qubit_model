from config import creatLeftHamiltonian


def termo_field_ouble(hamiltonian):
    eigenvalues, eigenvectors = hamiltonian.eigenstates()
    psi = sum([np.exp(-0.5 * e) * v for e, v in zip(eigenvalues, eigenvectors)])
    return psi.unit()

