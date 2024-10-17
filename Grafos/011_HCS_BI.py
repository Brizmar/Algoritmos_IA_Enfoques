import random

# Función de evaluación (heurística)
def funcion_evaluacion(estado):
    # Ejemplo: función cuadrática para maximizar
    return -(estado - 3) ** 2 + 10  # Pico en estado=3

# Generar vecinos cercanos (perturbaciones pequeñas)
def generar_vecinos(estado):
    return [estado - 1, estado + 1]

# Algoritmo de búsqueda de ascensión de colinas
def ascension_colinas(estado_inicial, iteraciones_max=100):
    estado_actual = estado_inicial
    for i in range(iteraciones_max):
        vecinos = generar_vecinos(estado_actual)
        mejor_vecino = max(vecinos, key=funcion_evaluacion)
        
        # Si el mejor vecino es mejor que el estado actual, moverse a él
        if funcion_evaluacion(mejor_vecino) > funcion_evaluacion(estado_actual):
            estado_actual = mejor_vecino
        else:
            # Hemos alcanzado un máximo local
            break
    return estado_actual

# Ejemplo de uso
estado_inicial = random.randint(-10, 10)
solucion = ascension_colinas(estado_inicial)
print(f"Estado inicial: {estado_inicial}, Solución encontrada: {solucion}")
