# Constraint Propagation Algorithms -> Propagacion de Restricciones
def ac3(csp):
    queue = [(xi, xj) for xi in csp.variables for xj in csp.constraints[xi]]
    
    while queue:
        (xi, xj) = queue.pop(0)
        if revise(csp, xi, xj):
            if not csp.domains[xi]:
                return False  # Dominio vacío, no hay solución
            for xk in csp.constraints[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(csp, xi, xj):
    revised = False
    for x in csp.domains[xi]:
        if not any(csp.is_consistent(x, y) for y in csp.domains[xj]):
            csp.domains[xi].remove(x)
            revised = True
    return revised
