import random

#Travelling Salesman Problem

# Función objetivo (ejemplo): calcular el costo de una solución
def funcion_objetivo(solucion):
    # Simulación de una función de costo para el ejemplo (suma de los valores)
    return sum(solucion)

# Generar vecinos cercanos (intercambia dos elementos de la lista)
def generar_vecinos(solucion):
    vecinos = []
    for i in range(len(solucion)):
        for j in range(i+1, len(solucion)):
            vecino = solucion[:]
            vecino[i], vecino[j] = vecino[j], vecino[i]  # Intercambiar dos elementos
            vecinos.append(vecino)
    return vecinos

# Algoritmo de búsqueda tabú
def busqueda_tabu(solucion_inicial, max_iteraciones=100, tamano_tabu=5):
    solucion_actual = solucion_inicial
    mejor_solucion = solucion_inicial[:]
    lista_tabu = []

    for iteracion in range(max_iteraciones):
        vecinos = generar_vecinos(solucion_actual)
        
        # Excluir movimientos tabú
        vecinos_validos = [vec for vec in vecinos if vec not in lista_tabu]
        
        # Si todos los vecinos son tabú, permitir el mejor vecino (criterio de aspiración)
        if not vecinos_validos:
            vecinos_validos = vecinos
        
        # Seleccionar el mejor vecino basado en la función objetivo
        mejor_vecino = min(vecinos_validos, key=funcion_objetivo)
        
        # Actualizar la solución actual
        solucion_actual = mejor_vecino
        
        # Actualizar la lista tabú
        lista_tabu.append(mejor_vecino)
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0)  # Mantener el tamaño de la lista tabú
        
        # Actualizar la mejor solución encontrada
        if funcion_objetivo(mejor_vecino) < funcion_objetivo(mejor_solucion):
            mejor_solucion = mejor_vecino
    
    return mejor_solucion

# Ejemplo de uso
solucion_inicial = [random.randint(1, 100) for _ in range(5)]
print(f"Solución inicial: {solucion_inicial}, Costo: {funcion_objetivo(solucion_inicial)}")
mejor_solucion = busqueda_tabu(solucion_inicial)
print(f"Mejor solución encontrada: {mejor_solucion}, Costo: {funcion_objetivo(mejor_solucion)}")
