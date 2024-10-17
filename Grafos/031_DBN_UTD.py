# Redes Bayesiandas Dinámicas
from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# Definimos el modelo DBN
modelo = DBN()

# Agregar nodos para los estados en los tiempos t=0 y t=1
modelo.add_edges_from([(('clima', 0), ('clima', 1)), (('lluvia', 0), ('lluvia', 1))])

# CPD del estado inicial (t=0)
cpd_clima_0 = TabularCPD(variable=('clima', 0), variable_card=2, values=[[0.7], [0.3]])
cpd_lluvia_0 = TabularCPD(variable=('lluvia', 0), variable_card=2, values=[[0.8], [0.2]])

# CPD para el estado en t=1 dado t=0
cpd_clima_1 = TabularCPD(
    variable=('clima', 1), variable_card=2,
    values=[[0.8, 0.2], [0.3, 0.7]],
    evidence=[('clima', 0)], evidence_card=[2]
)

cpd_lluvia_1 = TabularCPD(
    variable=('lluvia', 1), variable_card=2,
    values=[[0.6, 0.4], [0.4, 0.6]],
    evidence=[('lluvia', 0)], evidence_card=[2]
)

# Añadimos los CPDs al modelo
modelo.add_cpds(cpd_clima_0, cpd_lluvia_0, cpd_clima_1, cpd_lluvia_1)

# Inferencia sobre la DBN
inferencia = DBNInference(modelo)
resultado = inferencia.forward_inference([('clima', 1)])

print("Probabilidades en t=1:", resultado)
