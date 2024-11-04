# Arboles de Decisión: ID3
from math import log2
import pandas as pd

# Función para calcular la entropía de un conjunto de datos
def entropy(data):
    labels = data.iloc[:, -1]
    label_counts = labels.value_counts()
    total = len(labels)
    return sum(-count/total * log2(count/total) for count in label_counts)

# Calcular la ganancia de información
def info_gain(data, feature):
    total_entropy = entropy(data)
    values = data[feature].value_counts(normalize=True)
    feature_entropy = sum(p * entropy(data[data[feature] == v]) for v, p in values.items())
    return total_entropy - feature_entropy

# Construcción del árbol de decisión
def id3(data, features):
    labels = data.iloc[:, -1]
    
    # Condiciones de parada
    if len(labels.unique()) == 1:
        return labels.iloc[0]
    if not features:
        return labels.mode()[0]
    
    # Seleccionar la mejor característica según la ganancia de información
    gains = {feature: info_gain(data, feature) for feature in features}
    best_feature = max(gains, key=gains.get)
    
    # Crear subárboles
    tree = {best_feature: {}}
    remaining_features = [f for f in features if f != best_feature]
    for value in data[best_feature].unique():
        subtree_data = data[data[best_feature] == value]
        subtree = id3(subtree_data, remaining_features)
        tree[best_feature][value] = subtree
    
    return tree

# Ejemplo de datos
data = pd.DataFrame({
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

# Construcción del árbol usando ID3
tree = id3(data, features=['Outlook', 'Humidity', 'Wind'])
print(tree)