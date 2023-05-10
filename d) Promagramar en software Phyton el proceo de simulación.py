import numpy as np

# Definir las entradas y los pesos sinápticos
x1 = np.array([1, 1, 1, 1])
x2 = np.array([1, -1, 1, -1])
x3 = np.array([1, -1, -1, -1])
x4 = np.array([1, -1, 1, 1])

w1 = np.array([1, 1, 1, 1])    # Pesos sinápticos de la neurona 1
w2 = np.array([1, -1, 1, -1])  # Pesos sinápticos de la neurona 2
w3 = np.array([1, -1, -1, -1]) # Pesos sinápticos de la neurona 3
w4 = np.array([1, -1, 1, 1])    # Pesos sinápticos de la neurona 4

# Definir la función de activación
def funcion_activacion(x):
    return 1 if x >= 0 else -1

# Calcular la salida de la red neuronal para cada vector de entrada
salida1 = funcion_activacion(np.dot(x1, w1))
salida2 = funcion_activacion(np.dot(x2, w2))
salida3 = funcion_activacion(np.dot(x3, w3))
salida4 = funcion_activacion(np.dot(x4, w4))

# Imprimir las salidas
print("Salida de la neurona 1:", salida1)
print("Salida de la neurona 2:", salida2)
print("Salida de la neurona 3:", salida3)
print("Salida de la neurona 4:", salida4)
