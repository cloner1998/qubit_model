

def mutual_information(rho, qubits):
    rho_A = rho.ptrace([0, 1, qubits, qubits + 1])
    rho_1 = rho_A.ptrace([0, 2])
    rho_2 = rho_A.ptrace([1, 3])
    return rho_A.entropy() - rho_1.entropy() - rho_2.entropy()
