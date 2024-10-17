def buscar_grafo(grafo, inicio, objetivo, metodo='dfs'):
    visitados = set()  # Para evitar visitar el mismo nodo varias veces
    if metodo == 'dfs':
        return dfs(grafo, inicio, objetivo, visitados)
    elif metodo == 'bfs':
        return bfs(grafo, inicio, objetivo)

# Implementación de DFS
def dfs(grafo, nodo, objetivo, visitados):
    if nodo not in visitados:
        print(f"Visitando nodo: {nodo}")
        visitados.add(nodo)
        if nodo == objetivo:
            return True  # Se encontró el nodo objetivo
        for vecino in grafo[nodo]:
            if dfs(grafo, vecino, objetivo, visitados):
                return True
    return False

# Implementación de BFS
from collections import deque
def bfs(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([inicio])  # Cola para manejar los nodos
    while cola:
        nodo = cola.popleft()
        if nodo == objetivo:
            print(f"Nodo objetivo {objetivo} encontrado.")
            return True
        if nodo not in visitados:
            print(f"Visitando nodo: {nodo}")
            visitados.add(nodo)
            cola.extend(grafo[nodo])
    return False

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Realizando la búsqueda
buscar_grafo(grafo, 'A', 'F', metodo='dfs')  # Cambia a 'bfs' para usar BFS
