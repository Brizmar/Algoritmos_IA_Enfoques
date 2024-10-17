# Lógica Proposional - Sintaxis y Semantica: Tablas de verdad
from itertools import product

def generar_tabla(proposiciones, expresion):
    # Generar todas las combinaciones posibles de valores de verdad
    combinaciones = list(product([True, False], repeat=len(proposiciones)))
    
    # Imprimir encabezado de la tabla
    encabezado = " | ".join(proposiciones) + " | " + expresion
    print(encabezado)
    print("-" * len(encabezado))

    # Evaluar la expresión para cada combinación de valores de verdad
    for combinacion in combinaciones:
        # Crear un diccionario de asignaciones (p: True, q: False, ...)
        valores = dict(zip(proposiciones, combinacion))
        
        # Evaluar la expresión usando las asignaciones
        resultado = eval(expresion, {}, valores)
        
        # Imprimir la fila correspondiente
        valores_str = " | ".join(str(v).ljust(5) for v in combinacion)
        print(f"{valores_str} | {resultado}")

# Ejemplo de uso
proposiciones = ["p", "q"]
expresion = "(p and q) or not p"
generar_tabla(proposiciones, expresion)

