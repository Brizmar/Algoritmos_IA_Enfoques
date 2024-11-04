# Listas de Decisión: K-DL y K-DT
# Lista de reglas (K-DL) para clasificar el tipo de animal según sus características
def decision_list(animal):
    rules = [
        (lambda x: x["has_fur"] and x["lays_eggs"] == False, "Mammal"),
        (lambda x: x["can_fly"], "Bird"),
        (lambda x: x["lays_eggs"], "Reptile"),
        (lambda x: x["lives_in_water"], "Fish"),
        (lambda x: True, "Unknown")  # regla por defecto si ninguna otra coincide
    ]

    for rule, classification in rules:
        if rule(animal):
            return classification

# Ejemplo de entrada
animal_1 = {"has_fur": True, "lays_eggs": False, "can_fly": False, "lives_in_water": False}
animal_2 = {"has_fur": False, "lays_eggs": True, "can_fly": True, "lives_in_water": False}

print("Animal 1 clasificado como:", decision_list(animal_1))  # Salida: Mammal
print("Animal 2 clasificado como:", decision_list(animal_2))  # Salida: Bird
