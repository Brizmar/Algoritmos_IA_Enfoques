# Backward Chaining 
# Base de hechos
hechos = {'fiebre', 'tos'}

# Conjunto de reglas
reglas = {
    'resfriado': ('fiebre', 'tos'),
    'infeccion_garganta': ('dolor_garganta', 'fiebre')
}

def encadenamiento_hacia_atras(meta, hechos, reglas):
    if meta in hechos:
        return True
    if meta in reglas:
        premisas = reglas[meta]
        for premisa in premisas:
            if not encadenamiento_hacia_atras(premisa, hechos, reglas):
                return False
        return True
    return False

# Ejecutar encadenamiento hacia atrás para probar si se puede llegar a la meta
meta = 'resfriado'
resultado = encadenamiento_hacia_atras(meta, hechos, reglas)
print(f"¿Es posible alcanzar la meta '{meta}'?:", resultado)
