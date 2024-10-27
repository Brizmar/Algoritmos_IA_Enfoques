# STRIPS y ADL
import heapq

class Nodo:
    def __init__(self, estado, padre=None, costo=0, heuristica=0):
        self.estado = estado
        self.padre = padre
        self.costo = costo
        self.heuristica = heuristica
        self.f = costo + heuristica

    def __lt__(self, otro):
        return self.f < otro.f

def a_star(inicial, objetivo, vecinos, heuristica):
    frontera = []
    heapq.heappush(frontera, Nodo(inicial, costo=0, heuristica=heuristica[inicial]))
    explorados = set()

    while frontera:
        nodo_actual = heapq.heappop(frontera)

        if nodo_actual.estado == objetivo:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.estado)
                nodo_actual = nodo_actual.padre
            return camino[::-1]  # devolver el camino en orden

        explorados.add(nodo_actual.estado)

        for vecino in vecinos[nodo_actual.estado]:
            if vecino not in explorados:
                costo_nuevo = nodo_actual.costo + 1  # Suponiendo costo uniforme
                heuristica_nueva = heuristica[vecino]
                nuevo_nodo = Nodo(vecino, padre=nodo_actual, costo=costo_nuevo, heuristica=heuristica_nueva)
                heapq.heappush(frontera, nuevo_nodo)

    return None  # No se encontró un camino

# Ejemplo de uso
vecinos = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

heuristicas = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

resultado = a_star('A', 'F', vecinos, heuristicas)
print("Camino encontrado:", resultado)