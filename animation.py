
from tkinter import *
import openai
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt 
import numpy as np

# Crear una figura
fig = plt.figure()

# Generar datos
x = np.linspace(0, 20, 100) 
y = np.sin(x)

# Crear una línea
line, = plt.plot(x, y, color='blue')

# Función de actualización de la animación
def animate(i): line.set_ydata(np.sin(x + i/10.0)) # Actualizar datos return line,

# Llamar a la función de la animación
ani = matplotlib.animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

plt.show()