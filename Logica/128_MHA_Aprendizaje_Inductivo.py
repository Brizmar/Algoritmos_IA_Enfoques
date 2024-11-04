# Mejor Hipótesis Actual
# Definir el conjunto de datos y un conjunto de hipótesis
dataset = [
    {"features": [1, 0, 1], "label": 1},
    {"features": [0, 1, 0], "label": 0},
    {"features": [1, 1, 1], "label": 1},
    {"features": [0, 0, 0], "label": 0}
]

# Conjunto de hipótesis (aquí, algunas reglas lógicas sencillas)
hypotheses = [
    lambda x: x[0] == 1,  # Hipótesis 1: la primera característica es 1
    lambda x: x[1] == 1,  # Hipótesis 2: la segunda característica es 1
    lambda x: sum(x) > 1  # Hipótesis 3: la suma de características es mayor a 1
]

# Encontrar la mejor hipótesis
def best_hypothesis(dataset, hypotheses):
    best_hypothesis = None
    best_accuracy = 0

    for hypothesis in hypotheses:
        correct_predictions = sum(1 for data in dataset if hypothesis(data["features"]) == data["label"])
        accuracy = correct_predictions / len(dataset)

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_hypothesis = hypothesis

    return best_hypothesis, best_accuracy

# Encontrar y mostrar la mejor hipótesis y su precisión
best_hyp, accuracy = best_hypothesis(dataset, hypotheses)
print("Mejor hipótesis encontrada con precisión:", accuracy) 
