from typing import Optional

import qutip as qt
from qutip.core import Qobj

def create_left_hamiltonian(number_of_qubits: int) -> Qobj:
    # Create the Hamiltonian for the L system
    hamiltonian: Optional[Qobj] = None

    sx = qt.sigmax()
    sy = qt.sigmay()
    sz = qt.sigmaz()

    for i in range(number_of_qubits - 1):
        # Interaction terms
        hamiltonian += qt.tensor([sx if j == i or j == i + 1 else qt.qeye(2) for j in range(number_of_qubits)])
        hamiltonian += qt.tensor([sy if j == i or j == i + 1 else qt.qeye(2) for j in range(number_of_qubits)])
        hamiltonian += qt.tensor([sz if j == i or j == i + 1 else qt.qeye(2) for j in range(number_of_qubits)])

        # Single qubit terms
        hamiltonian += -1.05 * qt.tensor([sx if j == i else qt.qeye(2) for j in range(number_of_qubits)])
        hamiltonian += 0.5 * qt.tensor([sz if j == i else qt.qeye(2) for j in range(number_of_qubits)])

    # Last qubit single terms beacuse of i + 1 in interaction terms that can not exceed 10
    hamiltonian += -1.05 * qt.tensor([sx if j == number_of_qubits - 1 else qt.qeye(2) for j in range(number_of_qubits)])
    hamiltonian += 0.5 * qt.tensor([sz if j == number_of_qubits - 1 else qt.qeye(2) for j in range(number_of_qubits)])

    return hamiltonian
