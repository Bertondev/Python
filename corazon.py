import matplotlib.pyplot as plt
import numpy as np

# Generar coordenadas para dibujar el corazón
t = np.linspace(0, 2*np.pi, 1000)
x = 16*np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# Crear figura y ejes
fig, ax = plt.subplots()

# Establecer límites de los ejes
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])

# Dibujar el corazón
ax.plot(x, y, 'r')

# Dibujar el avión
for i in range(len(x)-10):
    if i % 10 == 0:
        ax.plot(x[i:i+10], y[i:i+10], 'k')
        ax.arrow(x[i+9], y[i+9], x[i+10]-x[i+9], y[i+10]-y[i+9], head_width=1, head_length=1, fc='k', ec='k')

# Mostrar la figura
plt.show()
