from startup.startup import spins_spin_correlation_list, t_list
import matplotlib.pyplot as plt


def spin_spin_correlation_plot():
    plt.figure(figsize=(10, 6))
    plt.plot(t_list, spins_spin_correlation_list, label='Spin-Spin Correlation')
    plt.xlabel('tw')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Spin-Spin Correlation vs tw')
    plt.show()
