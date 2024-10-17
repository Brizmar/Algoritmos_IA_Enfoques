# Equilibrios de Nash
import nashpy as nash
import numpy as np

# Definimos las matrices de pagos para dos jugadores
pago_jugador1 = np.array([[3, 1], [0, 2]])  # Pago para jugador 1
pago_jugador2 = np.array([[3, 0], [1, 2]])  # Pago para jugador 2

# Crear el juego bimatriz
juego = nash.Game(pago_jugador1, pago_jugador2)

# Calcular los equilibrios de Nash
equilibrios = list(juego.support_enumeration())

print("Equilibrios de Nash:")
for equilibrio in equilibrios:
    estrategia_j1, estrategia_j2 = equilibrio
    print(f"Estrategia Jugador 1: {estrategia_j1}, Estrategia Jugador 2: {estrategia_j2}")
