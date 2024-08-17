import qutip as qt


def create_left_hamiltonian(numberOfQubits):
    # Create the Hamiltonian for the L system
    hamiltonian = 0

    sx = qt.sigmax()
    sy = qt.sigmay()
    sz = qt.sigmaz()

    for i in range(numberOfQubits - 1):
        # Interaction terms
        hamiltonian += qt.tensor([sx if j == i or j == i + 1 else qt.qeye(2) for j in range(numberOfQubits)])
        hamiltonian += qt.tensor([sy if j == i or j == i + 1 else qt.qeye(2) for j in range(numberOfQubits)])
        hamiltonian += qt.tensor([sz if j == i or j == i + 1 else qt.qeye(2) for j in range(numberOfQubits)])

        # Single qubit terms
        hamiltonian += -1.05 * qt.tensor([sx if j == i else qt.qeye(2) for j in range(numberOfQubits)])
        hamiltonian += 0.5 * qt.tensor([sz if j == i else qt.qeye(2) for j in range(numberOfQubits)])

    # Last qubit single terms
    hamiltonian += -1.05 * qt.tensor([sx if j == numberOfQubits - 1 else qt.qeye(2) for j in range(numberOfQubits)])
    hamiltonian += 0.5 * qt.tensor([sz if j == numberOfQubits - 1 else qt.qeye(2) for j in range(numberOfQubits)])

    return hamiltonian