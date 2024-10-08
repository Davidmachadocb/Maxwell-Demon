import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def plot_entropia_temperatura(times, entropy_values, temperature_values, temperature_azul, temperature_vermelha):
    # Cria uma nova figura para entropia e temperatura
    entropy_temp_fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Plota a entropia
    ax1.plot(times, entropy_values, label='Entropia', color='purple')
    ax1.set_title("Entropia ao Longo do Tempo")
    ax1.set_ylabel("Entropia (Joules/Kelvin)")
    ax1.grid(True)
    ax1.legend()

    # Plota as temperaturas
    ax2.plot(times, temperature_values, label='Temperatura Total', color='orange')
    ax2.plot(times, temperature_azul, label='Temperatura Caixa Azul', color='blue')
    ax2.plot(times, temperature_vermelha, label='Temperatura Caixa Vermelha', color='red')
    ax2.set_title("Temperatura ao Longo do Tempo")
    ax2.set_xlabel("Tempo (s)")
    ax2.set_ylabel("Temperatura (Kelvin)")
    ax2.grid(True)
    ax2.legend()

    # Ajusta o layout e exibe o gráfico
    entropy_temp_fig.tight_layout()
    plt.show()
