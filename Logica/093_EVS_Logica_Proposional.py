# Equivalencia, Validez y Satisfacibilidad no es un algoritmo por si mismo 
from sympy import symbols
from sympy.logic.boolalg import Or, And, Not, Equivalent
from sympy.logic.inference import satisfiable

# Definir símbolos
P, Q = symbols('P Q')

# Definir proposiciones
proposicion1 = Or(P, Not(P))  # Tautología (siempre verdadero)
proposicion2 = And(P, Q)  # Solo verdadero si P y Q son verdaderos

# Verificar equivalencia entre dos proposiciones
equivalentes = Equivalent(proposicion1, proposicion2)
print("¿Son equivalentes?", equivalentes)

# Chequear validez (si es siempre verdadero)
validez = proposicion1.is_True
print("¿Es válida?", validez)

# Chequear satisfacibilidad (si puede ser verdadero en alguna situación)
satisfacibilidad = satisfiable(proposicion2)
print("¿Es satisfacible?", satisfacibilidad)