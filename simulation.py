#
#   Nome: David Machado
#   Graduação: Engenharia de Computação
#   Descrição: Este script executa uma simulação de partículas em um espaço bidimensional,
#              permitindo a visualização da evolução de energia cinética, entropia e 
#              temperatura do sistema sob diferentes tipos de colisões (elásticas e inelásticas).
#
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from particle import Particle
import numpy as np
from entropy import calculate_entropy, calculate_temperature, calculate_spatial_entropy, resolve_collision_elastic, resolve_collision_inelastic
from plots import plot_entropia_temperatura

def run_simulation(collision_type):
    # Configuração inicial da simulação e da figura
    fig, ax1 = plt.subplots(figsize=(6, 6))

    # Parâmetros das partículas
    numero_de_particulas = 50

    velocidade_maxima = 20  # Máxima magnitude da velocidade
    raio_particula = 0.05  # Raio padrão da partícula

    particles = []
    for _ in range(numero_de_particulas):
        # Gera uma posição aleatória, evitando as extremidades da caixa
        posicao_x = np.random.uniform(raio_particula, 2 - raio_particula)
        posicao_y = np.random.uniform(raio_particula, 2 - raio_particula)
        posicao = [posicao_x, posicao_y]

        # Gera uma velocidade aleatória em cada direção
        velocidade_x = np.random.uniform(-velocidade_maxima, velocidade_maxima)
        velocidade_y = np.random.uniform(-velocidade_maxima, velocidade_maxima)
        velocidade = [velocidade_x, velocidade_y]

        # Cria a partícula com posição e velocidade aleatórias
        particle = Particle(posicao, velocidade, 2, raio_particula)
        particles.append(particle)

    dt = 1/1000 # Intervalo de tempo para a simulação
    porta_x = 1
    ax1.axvline(x=porta_x, color='grey', linestyle='--')  # Linha vertical na posição x = 1
    frame_counter = [0]

    # Inicialização de variáveis para cálculo de entropia e temperatura
    times = []
    entropy_values = []
    smoothed_entropy = []
    temperature_values = []
    temperature_azul = []
    temperature_vermelha = []

    # Cria círculos para representar as partículas no gráfico
    circles = [plt.Circle(p.position, p.radius, color='blue') for p in particles]
    for circle in circles:
        ax1.add_patch(circle)
    ax1.set_xlim(0, 2)
    ax1.set_ylim(0, 2)
    ax1.set_aspect('equal', 'box')
    velocidade_limite = 10  # Velocidade limite para a partícula passar pela porta

    def update(frame):
        frame_counter[0] += 1

        for i, p in enumerate(particles):
            p.move(dt)
            cor = None  # Inicializa a variável cor

            # Verifica se a partícula está próxima da porta
            if porta_x - p.radius <= p.position[0] <= porta_x + p.radius:
                # Condição para partículas que se movem para a direita e têm velocidade alta
                if p.velocity[0] > 0 and np.linalg.norm(p.velocity) >= velocidade_limite:
                    cor = 'red'
                # Condição para partículas que se movem para a esquerda e têm velocidade baixa
                elif p.velocity[0] < 0 and np.linalg.norm(p.velocity) < velocidade_limite:
                    cor = 'blue'
                else:
                    # Reflete a partícula e atribui a cor correspondente
                    p.velocity[0] *= -1
                    cor = 'blue' if p.position[0] < porta_x else 'red'

            # Se a partícula não está perto da porta, define a cor baseada na velocidade
            if cor is None:
                cor = 'red' if np.linalg.norm(p.velocity) >= velocidade_limite else 'blue'

            circles[i].set_facecolor(cor)
            circles[i].center = p.position

        #colisoes
        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                if particles[i].check_collision(particles[j]):
                    if collision_type == 'elastic':
                        resolve_collision_elastic(particles[i], particles[j])
                    elif collision_type == 'inelastic':
                        resolve_collision_inelastic(particles[i], particles[j])
                    else:
                        raise ValueError("Invalid collision type specified")

        times.append(frame_counter[0])

        #temperatura
        temperature_caixa_azul = calculate_temperature(particles, region_limit=porta_x)
        temperature_caixa_vermelha = calculate_temperature([p for p in particles if p.position[0] >= porta_x])
        temperature_total = calculate_temperature(particles)
        temperature_values.append(temperature_total)
        temperature_azul.append(temperature_caixa_azul)
        temperature_vermelha.append(temperature_caixa_vermelha)
        #entropia
        entropy_values.append(calculate_spatial_entropy(particles))
        return circles

    ani = FuncAnimation(fig, update, frames=range(600), interval=50, blit=False)
    plt.show()

    plot_entropia_temperatura(times, entropy_values, temperature_values, temperature_azul, temperature_vermelha)

if __name__ == "__main__":
    run_simulation(collision_type='elastic')
