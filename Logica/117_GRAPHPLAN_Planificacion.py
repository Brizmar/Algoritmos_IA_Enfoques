# GRAPHPLAN
class GraphPlan:
    def __init__(self, acciones, estado_inicial, estado_objetivo):
        self.acciones = acciones
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.grafo = []

    def construir_grafo(self):
        # Implementación simplificada del grafo de planificación
        self.grafo.append([self.estado_inicial])
        
        # Aquí se construiría el grafo de acciones y estados...
        # Se omiten detalles de implementación por simplicidad

    def planificar(self):
        self.construir_grafo()
        # Lógica para verificar el grafo y encontrar el plan...
        # Se omiten detalles de implementación por simplicidad

# Ejemplo de uso
acciones = ['A1', 'A2', 'A3']  # Acciones posibles
estado_inicial = 'A'  # Estado inicial
estado_objetivo = 'B'  # Estado objetivo

graph_plan = GraphPlan(acciones, estado_inicial, estado_objetivo)
graph_plan.planificar()

# Aquí se puede implementar la lógica de búsqueda y generación de planes
print("Planificación completada.")
