# Planificacion de Orden Parcial
class PlanificacionOrdenParcial:
    def __init__(self):
        self.grafo = {}
        
    def agregar_accion(self, accion):
        if accion not in self.grafo:
            self.grafo[accion] = []

    def agregar_precedencia(self, accion1, accion2):
        if accion1 in self.grafo and accion2 in self.grafo:
            self.grafo[accion1].append(accion2)

    def obtener_plan(self):
        plan = []
        visitados = set()

        def dfs(accion):
            if accion not in visitados:
                visitados.add(accion)
                for siguiente in self.grafo[accion]:
                    dfs(siguiente)
                plan.append(accion)

        for accion in self.grafo.keys():
            dfs(accion)
        
        return plan[::-1]  # Invertir para obtener el orden correcto

# Ejemplo de uso
planificacion = PlanificacionOrdenParcial()
planificacion.agregar_accion('A')
planificacion.agregar_accion('B')
planificacion.agregar_accion('C')
planificacion.agregar_precedencia('A', 'C')

# Obtener el plan
plan = planificacion.obtener_plan()
print("Plan de ejecución:", plan)