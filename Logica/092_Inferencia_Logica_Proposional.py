# Inferencia Logica Proposicional
from sympy.logic.boolalg import Implies, Not, And
from sympy import symbols
from sympy.logic.inference import satisfiable

# Definir símbolos
P, Q = symbols('P Q')

# Inferencia: Si (P -> Q) y P, entonces Q
kb = [Implies(P, Q), P]  # Base de conocimiento

# Inferir Q
inferencia = Q

# Verificar si la inferencia es satisfacible con la base de conocimiento
resultado = satisfiable(And(*kb, Not(inferencia)))
print("¿Es válido inferir Q?", not resultado)

