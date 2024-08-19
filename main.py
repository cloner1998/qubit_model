from config import creatLeftHamiltonian
from startup import startup
import qutip as qt

from startup.startup import identity, hamiltonian

if __name__ == '__main__':
    startup.spin_spin_correlation_plot()
    startup.mutual_information_plot()
