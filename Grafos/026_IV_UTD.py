# Information of the value -> Valor de la informacion
import heapq

class Nodo:
    def __init__(self, nombre, costo, heuristica):
        self.nombre = nombre
        self.costo = costo  # Costo acumulado hasta el nodo
        self.heuristica = heuristica  # Heurística estimada al objetivo
        self.total = costo + heuristica  # Costo total estimado

    def __lt__(self, otro):
        return self.total < otro.total  # Comparar nodos por costo total

def busqueda_a_star(grafo, inicio, objetivo):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, Nodo(inicio, 0, grafo[inicio][objetivo]))  # Iniciar con el nodo de inicio

    explorados = set()  # Conjunto de nodos explorados

    while cola_prioridad:
        nodo_actual = heapq.heappop(cola_prioridad)

        # Si alcanzamos el objetivo, devolver el costo
        if nodo_actual.nombre == objetivo:
            return nodo_actual.costo

        explorados.add(nodo_actual.nombre)

        # Evaluar vecinos
        for vecino, costo in grafo[nodo_actual.nombre].items():
            if vecino not in explorados:
                heuristica = grafo[vecino][objetivo]  # Heurística del vecino al objetivo
                nuevo_nodo = Nodo(vecino, nodo_actual.costo + costo, heuristica)
                heapq.heappush(cola_prioridad, nuevo_nodo)

    return None  # No se encontró camino

# Definición del grafo (nodos, costos y heurísticas)
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 5, 'D': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

# Supongamos que la heurística es la distancia estimada en línea recta al objetivo
heuristicas = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 0
}

# Ejecutar búsqueda A*
costo_total = busqueda_a_star(grafo, 'A', 'F')
print(f"Costo total desde A hasta F: {costo_total}")
