from startup.startup import mutual_info_list, t_list
import matplotlib.pyplot as plt


def mutual_information_plot():
    plt.figure(figsize=(10, 6))
    plt.plot(t_list, mutual_info_list(), label='Mutual Information')
    plt.xlabel('tw')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Mutual Information vs tw')
    plt.show()
