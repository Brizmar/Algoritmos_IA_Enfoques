# Conflict-Directed Backjumping -> Salto Atrás Dirigido por Conflictos
class CDBJ_Sudoku:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.variables = [(i, j) for i in range(9) for j in range(9) if puzzle[i][j] == 0]
        self.domains = {var: set(range(1, 10)) for var in self.variables}
        self.conflicts = {var: set() for var in self.variables}  # Registra conflictos de cada variable

    def print_sudoku(self):
        """Imprime el Sudoku en un formato legible."""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                print(self.puzzle[i][j] if self.puzzle[i][j] != 0 else ".", end=" ")
            print()

    def is_consistent(self, var, value):
        """Verifica si la asignación es consistente con las reglas del Sudoku."""
        row, col = var

        # Verifica la fila y la columna
        for i in range(9):
            if self.puzzle[row][i] == value or self.puzzle[i][col] == value:
                return False

        # Verifica la subcuadrícula 3x3
        sub_row, sub_col = row // 3 * 3, col // 3 * 3
        for i in range(sub_row, sub_row + 3):
            for j in range(sub_col, sub_col + 3):
                if self.puzzle[i][j] == value:
                    return False

        return True

    def backtrack(self, index):
        """Implementa el algoritmo CDBJ para resolver el Sudoku."""
        if index == len(self.variables):
            return True  # Se ha encontrado una solución completa

        var = self.variables[index]

        # Itera sobre los valores posibles para la variable actual
        for value in self.domains[var]:
            if self.is_consistent(var, value):
                self.puzzle[var[0]][var[1]] = value

                # Intento recursivo con la siguiente variable
                if self.backtrack(index + 1):
                    return True

                # Si falla, restablece la variable
                self.puzzle[var[0]][var[1]] = 0

            else:
                # Registra un conflicto si el valor no es consistente
                self.conflicts[var].add(value)

        # Si no se encuentra solución válida, realiza salto atrás
        self.jump_back(index)
        return False

    def jump_back(self, index):
        """Realiza un salto atrás al último punto relevante de conflicto."""
        conflict_vars = [var for var in self.conflicts if self.conflicts[var]]
        if conflict_vars:
            # Encuentra la variable más cercana hacia atrás con conflictos
            last_conflict = max(conflict_vars, key=lambda v: self.variables.index(v))
            new_index = self.variables.index(last_conflict)
            print(f"Saltando atrás al índice {new_index} debido a conflictos.")
            return new_index

        return index - 1  # Retrocede un paso si no hay conflictos registrados

    def solve(self):
        """Inicia la resolución del Sudoku."""
        if self.backtrack(0):
            print("¡Sudoku resuelto!")
        else:
            print("No se encontró solución.")
        self.print_sudoku()


# Ejemplo de Sudoku para resolver
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Inicializa y resuelve el Sudoku con CDBJ
solver = CDBJ_Sudoku(puzzle)
solver.solve()
