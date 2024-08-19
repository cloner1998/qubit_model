import qutip as qt


def perturbation_function(qubits):
    # Define perturbation (σz on the 5th qubit of the L system).
    # the first and last part qt.qeye(2)] * 4 and qt.qeye(2)] * (2 * qubits - 5) are for do not change rest of the tensor
    perturbation = qt.tensor([qt.qeye(2)] * 4 + [qt.sigmaz()] + [qt.qeye(2)] * (2 * qubits - 5))
    return perturbation
