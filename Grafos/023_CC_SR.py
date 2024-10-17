# Cutoff Conditioning -> Acondicionamiento de Corte
class NQueensCSP:
    def __init__(self, N):
        self.N = N
        self.solution = None

    def is_valid(self, assignment, row, col):
        """Verifica si colocar una reina en (row, col) es válido."""
        for r, c in assignment.items():
            if c == col or abs(r - row) == abs(c - col):
                return False  # Conflicto detectado
        return True

    def backtrack(self, assignment={}, row=0, depth_limit=10):
        """Búsqueda con acondicionamiento de corte por profundidad."""
        if len(assignment) == self.N:
            self.solution = assignment
            return True  # Solución encontrada

        if row >= depth_limit:
            return False  # Corte: se alcanzó el límite de profundidad

        for col in range(self.N):
            if self.is_valid(assignment, row, col):
                assignment[row] = col
                if self.backtrack(assignment, row + 1, depth_limit):
                    return True
                del assignment[row]  # Deshacer asignación

        return False

    def solve(self):
        """Inicia la búsqueda con un límite de profundidad."""
        if self.backtrack():
            return self.solution
        else:
            print("No se encontró solución dentro del límite.")

# Ejemplo de uso
solver = NQueensCSP(8)
solution = solver.solve()
print("Solución:", solution)
  