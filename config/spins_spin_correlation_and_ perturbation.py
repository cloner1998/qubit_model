import qutip as qt


def spin_spin_correlation(psi, qubits):
    # Compute spin-spin correlation between first qubit and its double
    op = qt.tensor([qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1) + [qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1))
    return qt.expect(op, psi)


def perturbation_function(qubits):
    perturbation = qt.tensor([qt.qeye(2)]*4 + [qt.sigmaz()] + [qt.qeye(2)]*(2*qubits-5))
    return perturbation
