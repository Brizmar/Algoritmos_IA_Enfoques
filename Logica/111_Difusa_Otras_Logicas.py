# Conjuntos Difusos
import numpy as np
import matplotlib.pyplot as plt

# Función de membresía triangular
def triangular_membership(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

# Valores de la temperatura
x = np.linspace(0, 50, 100)

# Definir los puntos de la función de membresía (para "temperatura alta")
a, b, c = 25, 35, 45  # Entre 25°C y 45°C

# Calcular el grado de pertenencia
membership_values = triangular_membership(x, a, b, c)

# Graficar la función de membresía
plt.plot(x, membership_values, label='Temperatura alta')
plt.title('Función de Membresía Difusa - Temperatura Alta')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid(True)
plt.show()

