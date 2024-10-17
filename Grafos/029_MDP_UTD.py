# Proceso de decision de Markov
import numpy as np

# Parámetros del MDP
estados = ['A', 'B']
acciones = ['izquierda', 'derecha']
recompensas = {'A': 1, 'B': -1}
transiciones = {'A': {'izquierda': 'A', 'derecha': 'B'}, 'B': {'izquierda': 'A', 'derecha': 'B'}}
gamma = 0.9  # Factor de descuento

def iteracion_de_valores():
    V = {estado: 0 for estado in estados}
    while True:
        delta = 0
        for estado in estados:
            v = max(recompensas[estado] + gamma * V[transiciones[estado][accion]] for accion in acciones)
            delta = max(delta, abs(v - V[estado]))
            V[estado] = v
        if delta < 1e-4:
            break
    return V

print("Valores óptimos:", iteracion_de_valores())
