# Conjuntos de Hipótesis: Boosting
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar datos de ejemplo
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Configurar el clasificador AdaBoost
base_model = DecisionTreeClassifier(max_depth=1)
ada_boost = AdaBoostClassifier(base_estimator=base_model, n_estimators=50, learning_rate=1.0, random_state=42)

# Entrenar el modelo
ada_boost.fit(X_train, y_train)

# Realizar predicciones y calcular precisión
y_pred = ada_boost.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo AdaBoost: {accuracy * 100:.2f}%")

