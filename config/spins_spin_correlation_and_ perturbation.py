import qutip as qt


def spin_spin_correlation(psi, qubits):
    # Compute spin-spin correlation between first qubit and its double
    #for get a better idea please check erturbation_function
    op = qt.tensor([qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1) + [qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1))
    return qt.expect(op, psi)


def perturbation_function(qubits):
    # Define perturbation (σz on the 5th qubit of the L system).
    # the first and last part qt.qeye(2)] * 4 and qt.qeye(2)] * (2 * qubits - 5) are for do not change rest of the tensor
    perturbation = qt.tensor([qt.qeye(2)] * 4 + [qt.sigmaz()] + [qt.qeye(2)] * (2 * qubits - 5))
    return perturbation
