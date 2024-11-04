# Programación Lógica Inductiva: FOIL
# Ejemplo simplificado de FOIL en Python (no una implementación completa de FOIL)

import numpy as np
from sklearn.datasets import load_iris

# Cargar datos de ejemplo (iris dataset)
data = load_iris()
X = data.data
y = data.target

# Supongamos que queremos aprender una regla para identificar flores de clase 0
def learn_rule(X, y, target_class=0):
    rule = []
    # Convertir a binario: 1 si pertenece a la clase de interés, 0 en caso contrario
    target = (y == target_class).astype(int)
    num_features = X.shape[1]
    
    for feature_index in range(num_features):
        threshold = np.mean(X[:, feature_index])  # Simplemente un umbral promedio como ejemplo
        condition = f"Feature[{feature_index}] >= {threshold:.2f}"
        
        # Añadir condición a la regla si cubre más ejemplos positivos que negativos
        covered = (X[:, feature_index] >= threshold).astype(int)
        positives = np.sum((covered == 1) & (target == 1))
        negatives = np.sum((covered == 1) & (target == 0))
        
        if positives > negatives:
            rule.append(condition)
    
    return " AND ".join(rule)

# Aplicar el aprendizaje de regla
rule = learn_rule(X, y)
print(f"Regla aprendida: {rule}")

