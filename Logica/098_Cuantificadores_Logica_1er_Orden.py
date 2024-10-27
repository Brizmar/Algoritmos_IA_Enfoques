# Sintaxis y Semántica: Cuantificadores
# Conjunto de datos (dominio)
elementos = [1, 2, 3, 4, 5]

# Propiedad a evaluar
def propiedad(x):
    return x % 2 == 0  # Por ejemplo, evaluar si es par

# Cuantificador Universal
def cuantificador_universal(propiedad, elementos):
    return all(propiedad(x) for x in elementos)

# Cuantificador Existencial
def cuantificador_existencial(propiedad, elementos):
    return any(propiedad(x) for x in elementos)

# Evaluar cuantificadores
resultado_universal = cuantificador_universal(propiedad, elementos)
resultado_existencial = cuantificador_existencial(propiedad, elementos)

print("Cuantificador Universal (todos son pares):", resultado_universal)
print("Cuantificador Existencial (hay al menos un par):", resultado_existencial)
