# Definimos una función de utilidad para cada ruta
def utilidad_esperada(prob_rapidez, prob_bloqueo):
    utilidad_rapidez = 10  # Alta utilidad si la ruta es rápida
    utilidad_bloqueo = -5  # Penalización por bloqueos

    # Utilidad esperada
    return (prob_rapidez * utilidad_rapidez) + (prob_bloqueo * utilidad_bloqueo)

# Probabilidades para las dos rutas
probabilidades_ruta_A = {'rapidez': 0.8, 'bloqueo': 0.2}
probabilidades_ruta_B = {'rapidez': 0.5, 'bloqueo': 0.1}

# Calculamos la utilidad esperada para ambas rutas
utilidad_A = utilidad_esperada(probabilidades_ruta_A['rapidez'], 
                               probabilidades_ruta_A['bloqueo'])
utilidad_B = utilidad_esperada(probabilidades_ruta_B['rapidez'], 
                               probabilidades_ruta_B['bloqueo'])

# Selección de la ruta con mayor utilidad
if utilidad_A > utilidad_B:
    print(f"Elegir Ruta A con utilidad: {utilidad_A}")
else:
    print(f"Elegir Ruta B con utilidad: {utilidad_B}")
