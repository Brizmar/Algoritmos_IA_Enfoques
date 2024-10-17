# Decision Tree -> Redes de Decisión
# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Cargar el conjunto de datos de iris
iris = load_iris()
X = iris.data  # Características (longitud y ancho del sépalo y pétalo)
y = iris.target  # Etiquetas (especies de iris)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el clasificador de árbol de decisión
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predicciones = clf.predict(X_test)

# Evaluar la precisión del modelo
precision = np.mean(predicciones == y_test)
print(f"Precisión del modelo: {precision * 100:.2f}%")

# Visualizar el árbol de decisión
plt.figure(figsize=(12, 8))
tree.plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.title("Árbol de Decisión para Clasificación de Iris")
plt.show()
