from config import creatLeftHamiltonian, TFD, time_evolution
from startup import startup
import qutip as qt

from startup.startup import identity, hamiltonian, psi_0, t_list

if __name__ == '__main__':
    startup.mutual_information_plot()
    startup.spin_spin_correlation_plot()

