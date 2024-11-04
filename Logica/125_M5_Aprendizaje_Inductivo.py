# Arboles de Regresión: M5
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dividir el conjunto de datos en función de la variable con menor varianza
def best_split(data):
    X, y = data.iloc[:, :-1], data.iloc[:, -1]
    min_variance = float("inf")
    split_feature, split_value = None, None
    
    for feature in X.columns:
        for value in X[feature].unique():
            left_y = y[X[feature] <= value]
            right_y = y[X[feature] > value]
            variance = left_y.var() * len(left_y) + right_y.var() * len(right_y)
            if variance < min_variance:
                min_variance, split_feature, split_value = variance, feature, value

    return split_feature, split_value

# Construcción recursiva del árbol de regresión M5
def build_tree(data, min_samples=5, max_depth=10, depth=0):
    X, y = data.iloc[:, :-1], data.iloc[:, -1]
    
    # Condiciones de parada
    if len(y) <= min_samples or depth >= max_depth:
        model = LinearRegression().fit(X, y)
        return model

    # Mejor división
    split_feature, split_value = best_split(data)
    if split_feature is None:
        model = LinearRegression().fit(X, y)
        return model

    # Dividir el conjunto de datos
    left_data = data[data[split_feature] <= split_value]
    right_data = data[data[split_feature] > split_value]

    # Crear subárboles
    tree = {
        "feature": split_feature,
        "value": split_value,
        "left": build_tree(left_data, min_samples, max_depth, depth + 1),
        "right": build_tree(right_data, min_samples, max_depth, depth + 1)
    }
    return tree

# Predicción con el árbol de regresión M5
def predict_tree(tree, x):
    if isinstance(tree, LinearRegression):
        return tree.predict([x])[0]
    
    if x[tree["feature"]] <= tree["value"]:
        return predict_tree(tree["left"], x)
    else:
        return predict_tree(tree["right"], x)

# Ejemplo de datos
data = pd.DataFrame({
    'X1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'X2': [5, 4, 6, 3, 7, 2, 8, 1, 9, 0],
    'Y': [1.1, 1.9, 2.8, 4.1, 4.9, 6.1, 6.8, 8.1, 8.9, 10.2]
})

# Construir el árbol M5
tree = build_tree(data)

# Predicción
print(predict_tree(tree, [5, 7]))