# Tipos de Razonamiento y Aprendizaje
from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])  # Característica (Variable independiente)
y = np.array([1, 2, 3, 4, 5])            # Etiqueta (Variable dependiente)

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X, y)

# Predicción
prediction = model.predict([[6]])
print(f"Predicción para el valor 6: {prediction[0]}")