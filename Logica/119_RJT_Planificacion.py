# Redes Jerárquicas de Tareas
class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []
        
    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def display(self, level=0):
        print('  ' * level + f'- {self.name}')
        for subtask in self.subtasks:
            subtask.display(level + 1)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear tareas
    main_task = Task("Desarrollo del Proyecto")
    subtask1 = Task("Investigación")
    subtask2 = Task("Diseño")
    subtask3 = Task("Implementación")

    # Añadir subtareas
    main_task.add_subtask(subtask1)
    main_task.add_subtask(subtask2)
    main_task.add_subtask(subtask3)

    subtask1.add_subtask(Task("Revisar Literatura"))
    subtask1.add_subtask(Task("Entrevistar Expertos"))

    subtask2.add_subtask(Task("Diseñar Prototipo"))

    # Mostrar la red jerárquica de tareas
    main_task.display()
