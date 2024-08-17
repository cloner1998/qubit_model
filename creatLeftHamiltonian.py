import qutip as qt

def creat_left_hamiltonian():
    hamiltonian = 0
    qubits = 10
    sx = qt.sigmax()
    sz = qt.sigmaz()

    for i in range(qubits):
        # Single qubit terms
        hamiltonian += -1.05 * qt.tensor([sx])
        hamiltonian += 0.5 * qt.tensor([sz])
    for i in range(qubits - 1):
        # Last qubit single terms because of sigmaz(i) and sigma(i+1) does not anymore exist
        hamiltonian += qt.tensor([sz]) * qt.tensor([sz])

    return hamiltonian