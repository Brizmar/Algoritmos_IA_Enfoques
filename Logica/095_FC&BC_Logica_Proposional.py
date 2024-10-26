# Encadenamiento hacia atras y adelante (adelante)
# Base de Conocimiento con reglas (si P, entonces Q)
reglas = {
    'P': 'Q',
    'Q': 'R',
    'R': 'S'
}

# Hechos conocidos
hechos = ['P']

# Encadenamiento hacia adelante
def encadenamiento_hacia_adelante(hechos, reglas):
    nuevos_hechos = set(hechos)
    while True:
        nuevos = set()
        for hecho in nuevos_hechos:
            if hecho in reglas:
                nuevos.add(reglas[hecho])
        if nuevos.issubset(nuevos_hechos):
            break
        nuevos_hechos.update(nuevos)
    return nuevos_hechos

resultado = encadenamiento_hacia_adelante(hechos, reglas)
print("Hechos inferidos:", resultado)

