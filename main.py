import numpy as np
import qutip as qt

def creat_left_hamiltonian():
    hamiltonian = 0
    qubits = 10
    sx = qt.sigmax()
    sy = qt.sigmay()
    sz = qt.sigmaz()

    for i in range(qubits - 1):
        # Interaction terms
        hamiltonian += qt.tensor([sx if j == i or j == i + 1 else qt.qeye(2) for j in range(qubits)])
        hamiltonian += qt.tensor([sz if j == i or j == i + 1 else qt.qeye(2) for j in range(qubits)])

        # Single qubit terms
        hamiltonian += -1.05 * qt.tensor([sx if j == i else qt.qeye(2) for j in range(qubits)])
        hamiltonian += 0.5 * qt.tensor([sz if j == i else qt.qeye(2) for j in range(qubits)])

    # Last qubit single terms
    hamiltonian += -1.05 * qt.tensor([sx if j == qubits - 1 else qt.qeye(2) for j in range(qubits)])
    hamiltonian += 0.5 * qt.tensor([sz if j == qubits - 1 else qt.qeye(2) for j in range(qubits)])

    return hamiltonian