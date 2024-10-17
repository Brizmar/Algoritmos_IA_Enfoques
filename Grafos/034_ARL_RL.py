# Aprendizaje por Refuerzo Activo
import numpy as np

# Matriz de recompensas
recompensas = np.array([
    [0, -1, 0, 0],
    [-1, 0, -1, 10],
    [0, -1, 0, -1],
    [0, 10, -1, 0]
])

def politica_activa(episodios=100, gamma=0.9, alpha=0.1):
    estados = recompensas.shape[0]
    Q = np.zeros((estados, estados))  # Valores Q
    
    for _ in range(episodios):
        estado = np.random.randint(0, estados)
        while True:
            accion = np.argmax(Q[estado])  # Explota la mejor acción
            recompensa = recompensas[estado, accion]
            proximo_estado = accion
            
            # Actualiza el valor Q
            Q[estado, accion] += alpha * (recompensa + gamma * np.max(Q[proximo_estado]) - Q[estado, accion])
            
            if proximo_estado == estado:
                break
            estado = proximo_estado
    
    politica = np.argmax(Q, axis=1)
    return politica

politica_optima = politica_activa()
print("Política óptima:", politica_optima)
