# Espacio de Versiones y AQ
# Ejemplo de datos de entrenamiento
training_data = [
    {"features": [1, 0, 1], "label": 1},
    {"features": [0, 1, 0], "label": 0},
    {"features": [1, 1, 1], "label": 1},
    {"features": [0, 0, 0], "label": 0}
]

# Conjunto inicial de hipótesis (Espacio de Versiones)
hypotheses = [
    lambda x: x[0] == 1,  # Hipótesis 1
    lambda x: x[1] == 1,  # Hipótesis 2
    lambda x: sum(x) > 1, # Hipótesis 3
    lambda x: x[2] == 1   # Hipótesis 4
]

# Algoritmo de eliminación de candidatos (Algoritmo A)
def version_space(training_data, hypotheses):
    consistent_hypotheses = hypotheses[:]

    for data in training_data:
        consistent_hypotheses = [h for h in consistent_hypotheses if h(data["features"]) == data["label"]]
    
    return consistent_hypotheses

# Ejecutar el algoritmo y obtener el espacio de versiones
consistent_hypotheses = version_space(training_data, hypotheses)
print("Espacio de versiones restante:", consistent_hypotheses)
print("Número de hipótesis consistentes:", len(consistent_hypotheses))
