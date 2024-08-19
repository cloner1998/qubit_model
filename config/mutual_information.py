import qutip as qt

def mutual_information(densityMetrixOfAllSystem, qubits):
    #It traces out all qubits except the first two qubits of L (indices 0 and 1)
    #and their corresponding qubits in R (indices N and N+1).
    dm_A = densityMetrixOfAllSystem.ptrace([0, 1, qubits-1, qubits])
    dm_1 = dm_A.ptrace([0, 2])
    dm_2 = dm_A.ptrace([1, 3])
    return qt.entropy_vn(dm_1) + qt.entropy_vn(dm_2) - qt.entropy_vn(dm_A)
