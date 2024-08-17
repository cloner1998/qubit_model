

def time_evolution(psi, hamiltonian, t):
    # Time evolution operator
    time_evolution_operator = (-1j * hamiltonian * t).expm()
    return time_evolution_operator * psi
