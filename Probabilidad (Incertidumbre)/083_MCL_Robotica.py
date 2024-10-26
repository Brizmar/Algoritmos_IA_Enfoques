# Localizacion: Monte Carlo
import numpy as np
import random
import matplotlib.pyplot as plt

# Inicialización de parámetros
num_particles = 1000
world_size = 100  # Tamaño del entorno (1D)
measurement_noise = 1.0
movement_noise = 1.0

# Estado verdadero del robot
true_position = random.uniform(0, world_size)

# Inicialización de partículas aleatorias
particles = np.random.uniform(0, world_size, num_particles)

# Función para simular el movimiento del robot
def move_robot(position, movement):
    position += movement + random.gauss(0, movement_noise)
    return position % world_size

# Función para medir la distancia entre la posición verdadera y una partícula
def measurement_probability(measurement, particle):
    return np.exp(-((particle - measurement) ** 2) / (2 * measurement_noise ** 2))

# Simulación de localización Monte-Carlo
def monte_carlo_localization(true_position, move_steps):
    global particles
    
    for step in range(move_steps):
        # Simular el movimiento del robot
        true_position = move_robot(true_position, random.uniform(0, 1))
        
        # Movimiento de las partículas
        particles = [move_robot(p, random.uniform(0, 1)) for p in particles]
        
        # Medición
        measurement = true_position + random.gauss(0, measurement_noise)
        
        # Ponderación de las partículas según la medición
        weights = [measurement_probability(measurement, p) for p in particles]
        
        # Normalización de los pesos
        weights /= np.sum(weights)
        
        # Resampling de las partículas basado en los pesos
        indices = np.random.choice(range(num_particles), num_particles, p=weights)
        particles = [particles[i] for i in indices]
        
        # Visualización
        plt.hist(particles, bins=30, density=True)
        plt.axvline(x=true_position, color='r', label='True position')
        plt.title(f'Step {step + 1}')
        plt.show()

    return particles

# Ejecutar la localización Monte-Carlo con 10 pasos de movimiento
particles = monte_carlo_localization(true_position, 10)
