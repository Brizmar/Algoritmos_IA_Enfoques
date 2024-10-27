# Agentes logicos no es un  algoritmo por si mismo pero aqui hay un ejemplo donde se pueda mostrar
class AgenteLogico:
    def __init__(self):
        # Base de conocimiento: hechos iniciales
        self.conocimientos = {
            'sobre': [('C', 'B'), ('B', 'mesa'), ('A', 'mesa')],
            'libre': ['A', 'C'],
        }

    # Reglas lógicas para mover bloques
    def puede_mover(self, bloque1, bloque2):
        # El bloque1 y bloque2 deben estar libres, y no pueden ser el mismo
        return (bloque1 in self.conocimientos['libre'] and
                bloque2 in self.conocimientos['libre'] and
                bloque1 != bloque2)

    # Acción de mover el bloque
    def mover(self, bloque1, bloque2):
        if self.puede_mover(bloque1, bloque2):
            # Actualiza los hechos cuando el movimiento es válido
            self.conocimientos['sobre'] = [(bloque1, bloque2)] + [
                (b, s) for (b, s) in self.conocimientos['sobre'] if b != bloque1]
            self.conocimientos['libre'].remove(bloque2)
            self.conocimientos['libre'].append(bloque1)
            print(f"Movido {bloque1} sobre {bloque2}")
        else:
            print(f"No se puede mover {bloque1} sobre {bloque2}")

# Ejemplo de uso
agente = AgenteLogico()

# Consulta si es posible mover C sobre A y realiza el movimiento
if agente.puede_mover('C', 'A'):
    agente.mover('C', 'A')
else:
    print("No se puede mover C sobre A.")

