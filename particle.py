import numpy as np

class Particle:
    def __init__(self, position, velocity, mass, radius=0.05, restitution=1.0):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
        self.radius = radius
        self.restitution = restitution

    def move(self, dt):
        self.position += self.velocity * dt
        self.check_wall_collision()

    def check_wall_collision(self):
        box_limit_x = 2
        box_limit_y = 2
        epsilon = self.radius + 1e-6  # Adiciona uma pequena margem para evitar que a partícula fique presa

        # Verifica colisão com as paredes horizontais
        if self.position[0] <= epsilon:
            self.velocity[0] = abs(self.velocity[0])  # Garante que a velocidade seja positiva
            self.position[0] = epsilon  # Reposiciona a partícula fora da parede
        elif self.position[0] >= box_limit_x - epsilon:
            self.velocity[0] = -abs(self.velocity[0])  # Garante que a velocidade seja negativa
            self.position[0] = box_limit_x - epsilon  # Reposiciona a partícula fora da parede

        # Verifica colisão com as paredes verticais
        if self.position[1] <= epsilon:
            self.velocity[1] = abs(self.velocity[1])  # Garante que a velocidade seja positiva
            self.position[1] = epsilon  # Reposiciona a partícula fora da parede
        elif self.position[1] >= box_limit_y - epsilon:
            self.velocity[1] = -abs(self.velocity[1])  # Garante que a velocidade seja negativa
            self.position[1] = box_limit_y - epsilon  # Reposiciona a partícula fora da parede


    def check_collision(self, other):
        dist = np.linalg.norm(self.position - other.position)
        return dist <= (self.radius + other.radius)