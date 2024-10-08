import numpy as np

def calculate_entropy(velocities, bins=10):
    magnitudes = np.linalg.norm(velocities, axis=1)

    counts, _ = np.histogram(magnitudes, bins=bins, density=True)

    probabilities = counts / counts.sum()

    probabilities = probabilities[probabilities > 0]

    entropy = -np.sum(probabilities * np.log(probabilities))

    return entropy

def calculate_temperature(particles, region_limit=None):
    if region_limit is None:
        total_kinetic_energy = sum(0.5 * p.mass * np.linalg.norm(p.velocity)**2 for p in particles)
    else:
        # Calcula a temperatura apenas para partículas em uma região específica
        total_kinetic_energy = sum(
            0.5 * p.mass * np.linalg.norm(p.velocity)**2 
            for p in particles 
            if p.position[0] < region_limit
        )

    if total_kinetic_energy == 0:
        return 0  # Para evitar divisão por zero se não houver partículas na região

    num_particles = len([p for p in particles if p.position[0] < region_limit]) if region_limit else len(particles)
    average_kinetic_energy = total_kinetic_energy / num_particles
    temperature = (1/2) * average_kinetic_energy  # Assuming kB = 1
    return temperature

def calculate_spatial_entropy(particles, bins=(2, 2)):
    positions = np.array([p.position for p in particles])
    counts, _, _ = np.histogram2d(positions[:, 0], positions[:, 1], bins=bins)
    probabilities = counts.flatten() / np.sum(counts)
    probabilities = probabilities[probabilities > 0]
    spatial_entropy = -np.sum(probabilities * np.log(probabilities))
    return spatial_entropy

def resolve_collision_elastic(p1, p2):
    normal_vector = p1.position - p2.position
    normal_vector /= np.linalg.norm(normal_vector)

    relative_velocity = p1.velocity - p2.velocity

    velocity_along_normal = np.dot(relative_velocity, normal_vector)

    if velocity_along_normal > 0:
        return

    impulse = (2 * velocity_along_normal) / (p1.mass + p2.mass)

    p1.velocity -= (impulse * p2.mass) * normal_vector
    p2.velocity += (impulse * p1.mass) * normal_vector


def resolve_collision_inelastic(p1, p2):
    normal_vector = p1.position - p2.position
    normal_vector /= np.linalg.norm(normal_vector)

    relative_velocity = p1.velocity - p2.velocity

    velocity_along_normal = np.dot(relative_velocity, normal_vector)

    if velocity_along_normal > 0:
        return

    total_mass = p1.mass + p2.mass

    combined_velocity = (p1.velocity * p1.mass + p2.velocity * p2.mass) / total_mass

    p1.velocity = combined_velocity
    p2.velocity = combined_velocity