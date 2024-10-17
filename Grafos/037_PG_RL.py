import numpy as np

def policy_gradient(states, actions, num_episodes, learning_rate):
    """
    Algoritmo de gradient de políticas.

    :param states: Número de estados
    :param actions: Número de acciones
    :param num_episodes: Número de episodios de entrenamiento
    :param learning_rate: Tasa de aprendizaje
    :return: Política aprendida
    """
    # Inicializa los pesos de la política
    weights = np.zeros((states, actions))

    for episode in range(num_episodes):
        state = np.random.randint(0, states)  # Estado inicial aleatorio
        done = False
        rewards = []
        states_visited = []
        actions_taken = []

        # Recolecta experiencia
        while not done:
            # Selecciona la acción usando softmax
            action_probs = softmax(weights[state])
            action = np.random.choice(range(actions), p=action_probs)

            # Simula el ambiente (por simplicidad, se mueve al siguiente estado)
            next_state = (state + 1) % states  # Ejemplo simplificado
            reward = 1 if next_state == states - 1 else 0  # Recompensa por alcanzar el estado objetivo

            # Guarda la experiencia
            rewards.append(reward)
            states_visited.append(state)
            actions_taken.append(action)

            state = next_state  # Actualiza el estado

            # Termina si se alcanza el estado objetivo
            if state == states - 1:
                done = True

        # Actualiza la política
        for t in range(len(rewards)):
            G = sum(rewards[t:])  # Retorno acumulado
            weights[states_visited[t], actions_taken[t]] += learning_rate * G

    return np.argmax(weights, axis=1)

def softmax(x):
    """Calcula el softmax de un vector."""
    exp_x = np.exp(x - np.max(x))  # Estabiliza el cálculo
    return exp_x / exp_x.sum(axis=0)

# Ejemplo de uso
if __name__ == "__main__":
    n_states = 4
    n_actions = 2
    num_episodes = 1000
    learning_rate = 0.01

    learned_policy = policy_gradient(n_states, n_actions, num_episodes, learning_rate)
    print("Política aprendida:", learned_policy)
