# Min-Conflict -> Búsqueda Local: Mínimos-Conflictos
import random

class MinConflictsNQueens:
    def __init__(self, N):
        self.N = N
        self.board = [random.randint(0, N - 1) for _ in range(N)]  # Asignación inicial aleatoria

    def print_board(self):
        """Imprime el tablero en formato visual."""
        for i in range(self.N):
            row = ["Q" if self.board[j] == i else "." for j in range(self.N)]
            print(" ".join(row))
        print()

    def conflicts(self, col, row):
        """Calcula el número de conflictos para colocar una reina en (col, row)."""
        count = 0
        for c in range(self.N):
            if c != col:
                r = self.board[c]
                if r == row or abs(r - row) == abs(c - col):  # Mismo fila o diagonal
                    count += 1
        return count

    def min_conflicts(self, max_steps=1000):
        """Ejecuta el algoritmo de mínimos conflictos."""
        for step in range(max_steps):
            conflicted_vars = [c for c in range(self.N) if self.conflicts(c, self.board[c]) > 0]
            if not conflicted_vars:
                return True  # Solución encontrada

            # Selecciona una variable en conflicto aleatoriamente
            col = random.choice(conflicted_vars)

            # Busca el valor que minimice los conflictos
            min_conflict_row = min(range(self.N), key=lambda r: self.conflicts(col, r))
            self.board[col] = min_conflict_row  # Asigna el valor óptimo

        return False  # No se encontró solución en el límite de pasos

# Ejemplo de uso
N = 8  # Número de reinas
solver = MinConflictsNQueens(N)

if solver.min_conflicts():
    print("¡Solución encontrada!")
    solver.print_board()
else:
    print("No se encontró solución.")
