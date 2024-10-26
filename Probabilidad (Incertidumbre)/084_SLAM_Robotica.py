# Localizacion y mapeo simultaneos 
import numpy as np
import matplotlib.pyplot as plt
import random

# Inicialización de parámetros
num_particles = 100
world_size = (100, 100)  # Tamaño del entorno (2D)
sensor_range = 10.0
movement_noise = 0.5
measurement_noise = 1.0

# Estado verdadero del robot (posición inicial)
true_position = np.array([random.uniform(0, world_size[0]), random.uniform(0, world_size[1])])

# Inicialización de partículas (posición aleatoria)
particles = [np.array([random.uniform(0, world_size[0]), random.uniform(0, world_size[1])]) for _ in range(num_particles)]

# Mapa de características (puntos en el entorno)
landmarks = np.array([[20, 30], [50, 50], [80, 20]])

# Función para mover el robot y las partículas
def move(position, movement):
    new_position = position + movement + np.random.normal(0, movement_noise, size=2)
    new_position = np.clip(new_position, 0, world_size)
    return new_position

# Función para simular las mediciones de sensores (distancias a los landmarks)
def sense(position, landmarks):
    distances = np.linalg.norm(landmarks - position, axis=1)
    return distances + np.random.normal(0, measurement_noise, size=len(distances))

# Función de probabilidad de medición
def measurement_prob(measurement, particle, landmarks):
    predicted_distances = np.linalg.norm(landmarks - particle, axis=1)
    error = np.sum((predicted_distances - measurement) ** 2)
    return np.exp(-error / (2 * measurement_noise ** 2))

# Simulación de SLAM con FastSLAM
def fastslam(true_position, steps):
    global particles
    for step in range(steps):
        # Movimiento del robot
        movement = np.array([random.uniform(-1, 1), random.uniform(-1, 1)])
        true_position = move(true_position, movement)
        
        # Movimiento de partículas
        particles = [move(p, movement) for p in particles]
        
        # Sensado del entorno
        measurement = sense(true_position, landmarks)
        
        # Ponderación de partículas
        weights = [measurement_prob(measurement, p, landmarks) for p in particles]
        weights = np.array(weights) / np.sum(weights)
        
        # Resampling de partículas
        indices = np.random.choice(range(num_particles), num_particles, p=weights)
        particles = [particles[i] for i in indices]
        
        # Visualización del estado
        plt.scatter(landmarks[:, 0], landmarks[:, 1], color='red', label='Landmarks')
        plt.scatter(true_position[0], true_position[1], color='blue', label='True position')
        plt.scatter([p[0] for p in particles], [p[1] for p in particles], color='green', alpha=0.4, label='Particles')
        plt.legend()
        plt.title(f'SLAM Step {step + 1}')
        plt.xlim(0, world_size[0])
        plt.ylim(0, world_size[1])
        plt.show()

# Ejecutar SLAM con 10 pasos
fastslam(true_position, 10)
