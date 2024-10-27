# Vigilancia de Ejecución y Replanificación
class ExecutionMonitor:
    def __init__(self):
        self.expected_state = "Task 1"
        self.current_state = "Task 1"

    def update_current_state(self, new_state):
        self.current_state = new_state
        self.check_for_deviation()

    def check_for_deviation(self):
        if self.current_state != self.expected_state:
            print(f"Deviation detected! Expected: {self.expected_state}, Current: {self.current_state}")
            self.replan()

    def replan(self):
        # Generar un nuevo plan
        if self.current_state == "Task 2":
            self.expected_state = "Task 3"
            print("Replanning: Moving to Task 3")
        else:
            self.expected_state = "Task 1"
            print("Replanning: Returning to Task 1")

# Ejemplo de uso
if __name__ == "__main__":
    monitor = ExecutionMonitor()

    # Simulación de la ejecución
    monitor.update_current_state("Task 1")  # No hay desviación
    monitor.update_current_state("Task 2")  # Desviación detectada
    monitor.update_current_state("Task 1")  # No hay desviación
