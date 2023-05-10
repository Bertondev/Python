import numpy as np

# Crear un objeto ndarray de tamaño 20x20 con elementos aleatorios
arr = np.random.random((20, 20))

# Imprimir el ndarray completo
print("Matriz aleatoria:")
print(arr)

# Obtener el elemento máximo y mínimo
max_value = np.max(arr)
min_value = np.min(arr)

# Imprimir el valor máximo y mínimo
print("Valor máximo:", max_value)
print("Valor mínimo:", min_value)