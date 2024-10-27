# Inferencia Difusa
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables difusas
temperatura = ctrl.Antecedent(np.arange(0, 51, 1), 'temperatura')
velocidad_ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad_ventilador')

# Definir funciones de membresía para la temperatura
temperatura['baja'] = fuzz.trimf(temperatura.universe, [0, 0, 25])
temperatura['media'] = fuzz.trimf(temperatura.universe, [15, 25, 35])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [25, 50, 50])

# Definir funciones de membresía para la velocidad del ventilador
velocidad_ventilador['lenta'] = fuzz.trimf(velocidad_ventilador.universe, [0, 0, 50])
velocidad_ventilador['media'] = fuzz.trimf(velocidad_ventilador.universe, [30, 50, 70])
velocidad_ventilador['rapida'] = fuzz.trimf(velocidad_ventilador.universe, [50, 100, 100])

# Definir las reglas difusas
regla1 = ctrl.Rule(temperatura['baja'], velocidad_ventilador['lenta'])
regla2 = ctrl.Rule(temperatura['media'], velocidad_ventilador['media'])
regla3 = ctrl.Rule(temperatura['alta'], velocidad_ventilador['rapida'])

# Crear el sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
simulacion = ctrl.ControlSystemSimulation(sistema_control)

# Proporcionar una entrada de temperatura
simulacion.input['temperatura'] = 30

# Ejecutar la simulación
simulacion.compute()

# Mostrar el resultado de la velocidad del ventilador
print(f"Velocidad del ventilador: {simulacion.output['velocidad_ventilador']}%")

# Visualización de las funciones de membresía
temperatura.view()
velocidad_ventilador.view()