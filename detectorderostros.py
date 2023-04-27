import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("imagen_referencia.png")
img = np.mean(img, axis=2)  # Convertir a escala de grises
img = np.where(img < np.mean(img), 0, 1)  # Convertir a binario
N = img.size  # Cantidad de neuronas
W = np.zeros((N, N))  # Matriz de pesos

for i in range(N):
    for j in range(N):
        if i != j:
            W[i, j] = img[i] * img[j]

theta = 0.5 * np.sum(img) - np.dot(W.sum(axis=1), img)  # Umbral
W = W - np.diag(W.diagonal())  # Asegurarse de que los pesos diagonales sean 0
W /= N  # Normalizar los pesos

def hopfield_step(s, W, theta):
    h = np.dot(W, s) - theta
    s_new = np.where(h > 0, 1, 0)
    return s_new

s = img.flatten()  # Estado inicial
for i in range(10):  # Iterar para asegurarse de que la red esté estabilizada
    s = hopfield_step(s, W, theta)

img_rec = s.reshape(img.shape)  # Imagen reconstruida
img_nueva = plt.imread("imagen_nueva.png")
img_nueva = np.mean(img_nueva, axis=2)
img_nueva = np.where(img_nueva < np.mean(img_nueva), 0, 1)

s = img_nueva.flatten()  # Estado inicial
for i in range(10):  # Iterar para asegurarse de que la red esté estabilizada
    s = hopfield_step(s, W, theta)

img_rec_nueva = s.reshape(img_nueva.shape)  # Imagen reconstruida

fig, ax = plt.subplots(1, 2)
ax[0].imshow(img_nueva, cmap="gray")
ax[0].set_title("Imagen nueva")
ax[1].imshow(img_rec_nueva, cmap="gray")
ax[1].set_title("Imagen reconstruida")
plt.show()
