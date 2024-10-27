# Planificación Continua y Multiagente
import random
import time

class Agent:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def act(self):
        # Simulación de movimiento aleatorio
        self.position += random.choice([-1, 1])
        print(f"{self.name} is now at position {self.position}")

class Environment:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def run_simulation(self, steps):
        for _ in range(steps):
            print("New Step:")
            for agent in self.agents:
                agent.act()
            time.sleep(1)  # Pausa para simular tiempo entre acciones

# Ejemplo de uso
if __name__ == "__main__":
    env = Environment()
    
    # Crear agentes
    agent1 = Agent("Agent 1")
    agent2 = Agent("Agent 2")

    env.add_agent(agent1)
    env.add_agent(agent2)

    # Ejecutar la simulación
    env.run_simulation(5)
