from heapq import heappop, heappush

def busqueda_heuristica_general(grafo, inicio, objetivo, heuristica):
    """
    Realiza una búsqueda heurística general (Greedy Best-First Search).

    :param grafo: Diccionario que representa el grafo. Las claves son los nodos y los valores
                  son diccionarios de nodos vecinos con sus costos de transición.
    :param inicio: Nodo inicial desde donde comienza la búsqueda.
    :param objetivo: Nodo objetivo que se desea alcanzar.
    :param heuristica: Función heurística que toma un nodo y retorna una estimación
                       del costo desde ese nodo hasta el objetivo.
    :return: Lista que representa el camino desde el inicio hasta el objetivo. 
             Retorna None si no se encuentra un camino.
    """
    # Cola de prioridad basada en la heurística
    cola_prioridad = []
    heappush(cola_prioridad, (heuristica(inicio), inicio))
    
    # Diccionario para rastrear los predecesores de cada nodo
    predecesores = {inicio: None}
    
    # Conjunto para mantener los nodos visitados
    visitados = set()
    
    while cola_prioridad:
        # Extrae el nodo con la menor heurística
        _, nodo_actual = heappop(cola_prioridad)
        
        # Si el nodo actual es el objetivo, reconstruye el camino
        if nodo_actual == objetivo:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = predecesores[nodo_actual]
            return camino[::-1]  # Retorna el camino en orden inverso
        
        # Marca el nodo actual como visitado
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)
        
        # Expande los vecinos del nodo actual
        for vecino in grafo.get(nodo_actual, {}):
            if vecino not in visitados:
                predecesores[vecino] = nodo_actual
                heappush(cola_prioridad, (heuristica(vecino), vecino))
    
    # Si la cola se vacía sin encontrar el objetivo
    return None

# Ejemplo de uso

# Definición del grafo
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

# Definición de la heurística: distancia en línea recta al objetivo 'F'
heuristica = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

def h(nodo):
    """Función heurística que retorna la estimación desde el nodo hasta el objetivo."""
    return heuristica.get(nodo, float('inf'))

# Realizando la búsqueda heurística
camino = busqueda_heuristica_general(grafo, 'A', 'F', h)

if camino:
    print(f"Camino encontrado: {' -> '.join(camino)}")
else:
    print("No se encontró un camino hacia el objetivo.")
