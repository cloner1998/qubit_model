import qutip as qt


def spin_spin_correlation(psi, qubits):
    # Compute spin-spin correlation between first qubit and its double
    #for get a better idea please check erturbation_function
    op = qt.tensor([qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1) + [qt.sigmaz()] + [qt.qeye(2)] * (qubits - 1))
    return qt.expect(op, psi)

