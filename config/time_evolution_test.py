

def create_propagator(hamiltonian, t):
    """
    Create the propagator for a given Hamiltonian and time.

    Parameters:
    hamiltonian (Qobj): System Hamiltonian
    t (float): Time for propagation

    Returns:
    Qobj: Propagator
    """
    return (-1j * hamiltonian * t).expm()


def time_evolution_propagator(psi_0, hamiltonian, t):
    """
    Evolve the initial state psi_0 under the Hamiltonian for time t using a propagator.

    Parameters:
    psi_0 (Qobj): Initial quantum state
    hamiltonian (Qobj): System Hamiltonian
    t (float): Time to evolve

    Returns:
    Qobj: Evolved quantum state
    """
    U = create_propagator(hamiltonian, t)
    return U * psi_0


def create_propagators(hamiltonian, times):
    """
    Create propagators for a list of times.

    Parameters:
    hamiltonian (Qobj): System Hamiltonian
    times (array): List of times

    Returns:
    list: List of propagators
    """
    return [create_propagator(hamiltonian, t) for t in times]


def time_evolution_precomputed(psi_0, propagator):
    """
    Evolve the initial state using a pre-computed propagator.

    Parameters:
    psi_0 (Qobj): Initial quantum state
    propagator (Qobj): Pre-computed propagator

    Returns:
    Qobj: Evolved quantum state
    """
    return propagator * psi_0
