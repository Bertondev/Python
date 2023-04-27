import numpy as np
import matplotlib.pyplot as plt

# Definir las vocales como patrones de entrenamiento
vowels = {
    'a': [-1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1],
    'e': [-1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1],
    'i': [-1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1],
    'o': [-1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1],
    'u': [1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1]
}

# Definimos la función de actualización de la red
def update_rule(W, x):
    """
    Actualiza la red Hopfield con la regla de actualización síncrona
    utilizando el vector de pesos W y la entrada x.
    Devuelve el nuevo estado de la red.
    """
    return np.sign(np.dot(W, x))

# Entrenar la red Hopfield
n = len(vowels['i'])
W = np.zeros((n, n))
for v in vowels.values():
    # Calcular los pesos de la red utilizando la regla de Hebb
    W += np.outer(v, v)
np.fill_diagonal(W, 0) # Establecer los pesos diagonales a cero

# Generar una entrada incompleta o ruidosa
input_vowel = vowels['i'].copy()
input_vowel[2] = -1 # Cambiar un bit de la entrada original a -1
input_vowel[6] = -1 # Cambiar otro bit de la entrada original a -1
input_vowel[12] = -1 # Cambiar otro bit de la entrada original a -1

# Recuperar la vocal correspondiente
for i in range(10):
    # Actualizar la red con la entrada incompleta
    output_vowel = update_rule(W, input_vowel)
    # Si la salida es igual a la entrada, se ha alcanzado un estado estable
    if np.array_equal(output_vowel, input_vowel):
        break
    # En caso contrario, utilizar la salida como nueva entrada y seguir actualizando la red
    input_vowel = output_vowel

# Mostrar la entrada, la salida y la vocal original
input_vowel = np.reshape(input_vowel, (3, 5))
output_vowel = np.reshape(output_vowel, (3, 5))
original_vowel = np.reshape(vowels['i'], (3, 5))
plt.imshow(input_vowel, cmap='gray')
plt.title('Input')
plt.show()
plt.imshow(output_vowel, cmap='gray')
plt.title('Output')
plt.show()
plt.imshow(original_vowel, cmap='gray')
plt.title('Original')
plt.show()
