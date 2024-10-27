# Logica Temporal
from sympy import symbols, Implies, And

# Definir proposiciones
P, Q = symbols('P Q')

# Operadores de lógica temporal simulados
def always(P):
    return f"G({P})"

def eventually(P):
    return f"F({P})"

def next_state(P):
    return f"X({P})"

def until(P, Q):
    return f"({P}) U ({Q})"

# Fórmula: G (P -> F Q)
formula = always(Implies(P, eventually(Q)))

# Imprimir la fórmula temporal
print("Fórmula temporal:", formula)

