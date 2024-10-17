# Policy Iteration -> Iteracion de Politicas
import numpy as np

estados = ['A', 'B']
acciones = ['izquierda', 'derecha']
recompensas = {'A': 1, 'B': -1}
transiciones = {'A': {'izquierda': 'A', 'derecha': 'B'}, 'B': {'izquierda': 'A', 'derecha': 'B'}}
gamma = 0.9  # Factor de descuento

def evaluar_politica(politica, V):
    while True:
        delta = 0
        for estado in estados:
            accion = politica[estado]
            estado_sig = transiciones[estado][accion]
            v = recompensas[estado] + gamma * V[estado_sig]
            delta = max(delta, abs(v - V[estado]))
            V[estado] = v
        if delta < 1e-4:
            break

def mejorar_politica(V):
    nueva_politica = {}
    for estado in estados:
        max_accion = max(acciones, key=lambda a: recompensas[estado] + gamma * V[transiciones[estado][a]])
        nueva_politica[estado] = max_accion
    return nueva_politica

V = {estado: 0 for estado in estados}
politica = {estado: acciones[0] for estado in estados}

while True:
    evaluar_politica(politica, V)
    nueva_politica = mejorar_politica(V)
    if nueva_politica == politica:
        break
    politica = nueva_politica

print("Política óptima:", politica)
