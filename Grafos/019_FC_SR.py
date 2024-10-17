# Forward Checking -> Algoritmo de Comprobacion haca adelante
class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.solution = None

    def solve(self):
        assignment = {}
        self.solution = self.backtrack(assignment)
        return self.solution

    def backtrack(self, assignment):
        # Si todas las variables están asignadas, retornar la solución
        if len(assignment) == len(self.variables):
            return assignment

        # Seleccionar la siguiente variable no asignada
        var = self.select_unassigned_variable(assignment)

        # Intentar cada valor del dominio de la variable
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                # Aplicar comprobación hacia adelante
                if self.forward_check(var, value):
                    result = self.backtrack(assignment)
                    if result is not None:
                        return result
                # Deshacer la asignación si no tuvo éxito
                del assignment[var]

        return None

    def forward_check(self, var, value):
        """Elimina valores inconsistentes de los dominios."""
        for neighbor in self.constraints[var]:
            if value in self.domains[neighbor]:
                self.domains[neighbor].remove(value)
                if not self.domains[neighbor]:
                    return False  # Si un dominio queda vacío, retroceder
        return True

    def select_unassigned_variable(self, assignment):
        return [v for v in self.variables if v not in assignment][0]

    def order_domain_values(self, var, assignment):
        return self.domains[var]

    def is_consistent(self, var, value, assignment):
        for neighbor in self.constraints[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True
