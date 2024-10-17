import tkinter as tk
from collections import deque
import random

# Definición del árbol de decisiones
# Para la representación de este árbol de decisiones utilizamos un grafo donde cada nodo representa un tema
# y cada arista es la conexión entre los temas que dependen unos de otros
# Visto de otra forma, es un diccionario donde las claves son los nombres de los nodos y los valores 
# son los temas que dependen del nodo actual 
tree = {
    "Álgebra básica": ["Funciones básicas", "Pendiente de una recta", "Límites básicos"],
    "Funciones básicas": ["Definición de derivada"],
    "Pendiente de una recta": ["Definición de derivada"],
    "Límites básicos": ["Definición de derivada"],
    "Definición de derivada": ["Reglas de derivación"],
    "Reglas de derivación": ["Derivada de funciones trigonométricas", "Derivada de funciones exponenciales"],
    "Derivada de funciones trigonométricas": ["Derivadas implícitas"],
    "Derivada de funciones exponenciales": ["Derivadas implícitas"],
    "Derivadas implícitas": ["Derivadas de orden superior"],
    "Derivadas de orden superior": ["Tasa de cambio", "Optimización", "Concavidad y puntos de inflexión", "Teorema de Taylor"],
    "Tasa de cambio": [],
    "Optimización": [],
    "Concavidad y puntos de inflexión": [],
    "Teorema de Taylor": []
}

# Consejos personalizados según el tema
study_tips = {
    "Álgebra básica": [
        "Álgebra es la base de todo, ¡sigue adelante!",
        "Recuerda practicar operaciones con fracciones y ecuaciones simples."
    ],
    "Funciones básicas": [
        "Las funciones son como máquinas, ¡entiende qué hacen con los valores!",
        "Recuerda repasar la notación funcional y los gráficos."
    ],
    "Pendiente de una recta": [
        "La pendiente es clave para entender el cambio en las funciones.",
        "Repasa la fórmula de la pendiente: m = (y2 - y1) / (x2 - x1)."
    ],
    "Límites básicos": [
        "Los límites son esenciales para comprender el cálculo.",
        "Recuerda: un límite es solo el valor al que se aproxima una función."
    ],
    "Definición de derivada": [
        "La derivada es la tasa de cambio instantánea. ¡Piensa en cómo cambian las cosas!",
        "Repasa la definición formal de derivada y el concepto de límite."
    ],
    "Reglas de derivación": [
        "Las reglas de derivación te simplifican la vida. ¡Memorízalas bien!",
        "La regla del producto y la regla del cociente son esenciales."
    ],
    "Derivada de funciones trigonométricas": [
        "La derivada de las funciones trigonométricas puede ser confusa, ¡practica con ejemplos!",
        "Recuerda que la derivada de sin(x) es cos(x), ¡y viceversa!"
    ],
    "Derivada de funciones exponenciales": [
        "Las funciones exponenciales crecen rápido, ¡entiende bien su comportamiento!",
        "Recuerda que la derivada de e^x es e^x. ¡Fácil de recordar!"
    ],
    "Derivadas implícitas": [
        "La derivación implícita es útil cuando no puedes despejar y.",
        "Repasa cómo derivar ambos lados de una ecuación simultáneamente."
    ],
    "Derivadas de orden superior": [
        "Las derivadas de orden superior te ayudan a entender la aceleración y más.",
        "No te olvides de la notación: la segunda derivada es d²y/dx²."
    ]
}

# Clase que maneja la interfaz gráfica
class StudyApp:
    def __init__(self, root, tree, start):
        self.tree = tree
        self.queue = deque([start])  # Inicializamos la cola con el nodo de inicio
        self.visited = set()  # Nodos ya visitados

        # Configuración de la ventana principal
        self.root = root
        self.root.title("Guía de Estudio - Búsqueda en Anchura")
        
        # Etiqueta para mostrar el tema actual
        self.label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, pady=20)
        self.label.pack()

        # Etiqueta para mostrar consejos
        self.tip_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=400)
        self.tip_label.pack()

        # Botones de interacción
        self.yes_button = tk.Button(root, text="Sí", command=self.study_next)
        self.no_button = tk.Button(root, text="No", command=self.study_no)
        
        self.yes_button.pack(side="left", padx=20, pady=20)
        self.no_button.pack(side="right", padx=20, pady=20)
        
        # Iniciar con el primer tema
        self.study_next()

    def study_next(self):
        self.tip_label.config(text="")  # Limpiamos los consejos anteriores

        if self.queue:
            # Sacamos el primer nodo de la cola
            node = self.queue.popleft()

            if node not in self.visited:
                # Actualizamos la etiqueta con el nuevo tema
                self.label.config(text=f"¿Ya terminaste de estudiar el tema '{node}'?")
                self.current_node = node
                self.visited.add(node)  # Marcamos el nodo como visitado

                # Añadimos los hijos a la cola
                self.advance_queue()

        else:
            # Cuando terminamos de recorrer todo el árbol
            self.label.config(text="¡Has terminado todos los temas!")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def study_no(self):
        # Mostramos un consejo aleatorio relacionado con el tema actual
        if self.current_node in study_tips:
            tip = random.choice(study_tips[self.current_node])
            self.tip_label.config(text=f"Consejo: {tip}")
        else:
            self.tip_label.config(text="¡Tómate tu tiempo, todo lleva su ritmo!")
        
        # Mensaje para indicar que el usuario aún no ha terminado el tema
        self.label.config(text=f"Tómate tu tiempo para estudiar '{self.current_node}' antes de continuar.")

    def advance_queue(self):
        # Añadimos los nodos hijos a la cola si no han sido visitados
        for neighbor in self.tree[self.current_node]:
            if neighbor not in self.visited:
                self.queue.append(neighbor)

# Crear la ventana de Tkinter
root = tk.Tk()
app = StudyApp(root, tree, "Álgebra básica")
root.mainloop()
