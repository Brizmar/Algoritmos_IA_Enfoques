# Logicas de orden superior
from sympy import symbols, Function, ForAll, Implies, Exists

# Definición de símbolos y funciones
x, y = symbols('x y')
P = Function('P')

# Fórmula: ∀P ∀x (P(x) → ∃y P(y))
formula = ForAll(P(x), Implies(P(x), Exists(y, P(y))))

# Imprimir la fórmula
print(formula)