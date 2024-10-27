# Logica Modal
from sympy import symbols, And, Or, Not

# Definir proposiciones
P = symbols('P')
Q = symbols('Q')

# Modalidad básica (interpretada simbólicamente)
def necesario(P):
    return f"□({P})"

def posible(P):
    return f"◊({P})"

# Ejemplos de uso
formula1 = necesario(P)
formula2 = posible(Q)

print("Fórmula 1 (necesario):", formula1)
print("Fórmula 2 (posible):", formula2)

# Operaciones lógicas combinadas
combination = And(necesario(P), posible(Not(Q)))
print("Combinación lógica:", combination)

