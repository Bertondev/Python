import numpy as np

# Definir las entradas y las salidas deseadas
X = np.array([[1, 1, 1, 1],
              [1, -1, 1, -1],
              [1, -1, -1, -1],
              [1, -1, 1, 1]])

y_deseado = np.array([1, -1, -1, 1])

# Inicializar los pesos sinápticos de forma aleatoria
w = np.random.randn(4)

# Definir la función de activación
def funcion_activacion(x):
    return np.where(x >= 0, 1, -1)

# Definir la función de pérdida (cuadrática media)
def funcion_perdida(y, y_deseado):
    return np.mean((y - y_deseado)**2)

# Definir el algoritmo de aprendizaje (descenso de gradiente)
def descenso_gradiente(X, y_deseado, w, tasa_aprendizaje, epochs):
    for epoch in range(epochs):
        for i in range(len(X)):
            x = X[i]
            y = funcion_activacion(np.dot(x, w))
            error = y_deseado[i] - y
            delta_w = tasa_aprendizaje * error * x
            w += delta_w
        perdida = funcion_perdida(funcion_activacion(np.dot(X, w)), y_deseado)
        print("Época:", epoch + 1, "Pérdida:", perdida)
    return w

# Parámetros de aprendizaje
tasa_aprendizaje = 0.1
epochs = 100

# Aplicar el algoritmo de aprendizaje
w_optimizado = descenso_gradiente(X, y_deseado, w, tasa_aprendizaje, epochs)

# Imprimir los pesos sinápticos optimizados
print("Pesos sinápticos optimizados:", w_optimizado)
