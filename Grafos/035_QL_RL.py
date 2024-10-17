#Q-Learning
import numpy as np

# Definición del entorno
n_states = 16  # Número de estados en el grid world
n_actions = 4  # Número de acciones posibles (arriba, abajo, izquierda, derecha)
goal_state = 15  # Estado objetivo

# Inicialización de la Q-table con ceros
Q_table = np.zeros((n_states, n_actions))

# Definición de parámetros
learning_rate = 0.8
discount_factor = 0.95
exploration_prob = 0.2
epochs = 1000

# Algoritmo de Q-learning
for epoch in range(epochs):
    # Inicia desde un estado aleatorio
    current_state = np.random.randint(0, n_states)
    
    # Realiza iteraciones hasta alcanzar el estado objetivo
    while current_state != goal_state:
        # Estrategia epsilon-greedy para seleccionar la acción
        if np.random.rand() < exploration_prob:
            action = np.random.randint(0, n_actions)  # Explorar
        else:
            action = np.argmax(Q_table[current_state])  # Explotar
        
        # Simula el entorno (transición al siguiente estado)
        next_state = (current_state + 1) % n_states  # Para simplificar, avanza al siguiente estado

        # Definición de la función de recompensa
        reward = 1 if next_state == goal_state else 0

        # Actualización del valor Q usando la regla de actualización de Q-learning
        Q_table[current_state, action] += learning_rate * (
            reward + discount_factor * np.max(Q_table[next_state]) - Q_table[current_state, action]
        )

        # Mueve al siguiente estado
        current_state = next_state

# Muestra la Q-table aprendida
print("Learned Q-table:")
print(Q_table)
