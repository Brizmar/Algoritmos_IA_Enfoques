# Explicaciones e Información Relevante - No es un algoritmo por si mismo pero en relacion: SHAP
import shap
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Cargar datos y dividirlos en entrenamiento y prueba
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar un modelo de bosque aleatorio
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Crear valores SHAP para el conjunto de prueba
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Visualizar la importancia de las características para el primer ejemplo de prueba
shap.initjs()
shap.force_plot(explainer.expected_value[0], shap_values[0][0], X_test.iloc[0])
