# Lógica No Monotónica
class Bird:
    def __init__(self, name, can_fly=True):
        self.name = name
        self.can_fly = can_fly
    
    def add_info(self, new_info):
        if new_info == "penguin":
            self.can_fly = False

    def check_ability(self):
        if self.can_fly:
            return f"{self.name} can fly."
        else:
            return f"{self.name} cannot fly."

# Inicialmente asumimos que Tweety puede volar
tweety = Bird("Tweety")

# Imprimir la habilidad de Tweety
print(tweety.check_ability())  # "Tweety can fly."

# Agregar nueva información que Tweety es un pingüino
tweety.add_info("penguin")

# Verificar nuevamente después de la nueva información
print(tweety.check_ability())  # "Tweety cannot fly."