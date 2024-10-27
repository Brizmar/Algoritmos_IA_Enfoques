# Lógica por Defecto
class Bird:
    def __init__(self, name, is_special=False):
        self.name = name
        self.is_special = is_special
    
    def can_fly(self):
        # Regla por defecto: si no es un caso especial, se asume que puede volar
        if not self.is_special:
            return f"{self.name} can fly by default."
        else:
            return f"{self.name} cannot fly because it is a special case."

# Crear algunos pájaros
tweety = Bird("Tweety")  # Tweety es un pájaro normal
penguin = Bird("Penguin", is_special=True)  # Penguin es un caso especial

# Inferir si pueden volar
print(tweety.can_fly())   # Tweety puede volar por defecto
print(penguin.can_fly())  # Penguin no puede volar, es un caso especial