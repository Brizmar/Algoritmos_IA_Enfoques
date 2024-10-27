# Planificación Condicional
class Agent:
    def __init__(self):
        self.state = {}

    def update_state(self, condition, value):
        self.state[condition] = value

    def plan_action(self):
        if self.state.get('weather') == 'rainy':
            return "Take an umbrella"
        elif self.state.get('weather') == 'sunny':
            return "Wear sunglasses"
        else:
            return "Stay inside"

# Ejemplo de uso
if __name__ == "__main__":
    agent = Agent()

    # Simulación de condiciones
    agent.update_state('weather', 'rainy')
    action = agent.plan_action()
    print(f"Action based on condition: {action}")

    agent.update_state('weather', 'sunny')
    action = agent.plan_action()
    print(f"Action based on condition: {action}")

    agent.update_state('weather', 'cloudy')
    action = agent.plan_action()
    print(f"Action based on condition: {action}")