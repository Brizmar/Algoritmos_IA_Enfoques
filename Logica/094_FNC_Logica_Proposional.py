# Forma Normal Conjuntiva
from sympy import symbols
from sympy.logic.boolalg import Or, And, Not, to_cnf
from sympy.logic.inference import satisfiable

# Definir símbolos
P, Q, R = symbols('P Q R')

# Definir una proposición compleja
proposicion = Or(And(P, Q), Not(R))

# Convertir la proposición a Forma Normal Conjuntiva (FNC)
fnc_proposicion = to_cnf(proposicion)
print("Forma Normal Conjuntiva:", fnc_proposicion)

# Verificar satisfacibilidad mediante resolución
resultado = satisfiable(fnc_proposicion)
print("¿Es satisfacible mediante resolución?", resultado)
