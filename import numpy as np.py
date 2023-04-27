from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen original y convertirla a escala de grises
img = Image.open("hombre.jpg").convert('L')
img_arr = np.array(img)

# Agregar ruido aleatorio a la imagen
noise = np.random.randint(0, 2, size=img_arr.shape)
noisy_img_arr = np.where(noise == 1, img_arr + 50, img_arr)

# Crear la matriz de pesos para la red Hopfield
n_pixels = img_arr.shape[0] * img_arr.shape[1]
W = np.zeros((n_pixels, n_pixels))

for i in range(n_pixels):
    for j in range(i+1, n_pixels):
        W[i,j] = np.sum(noisy_img_arr.flatten()[i] * noisy_img_arr.flatten()[j])
        W[j,i] = W[i,j]

# Crear una función para limpiar la imagen ruidosa utilizando la red Hopfield
def clean_image(noisy_img_arr, W, iterations=5):
    n_pixels = noisy_img_arr.shape[0] * noisy_img_arr.shape[1] 
    for iteration in range(iterations):
        for i in range(n_pixels):
            activation = 0
            for j in range(n_pixels):
                activation += W[i,j] * noisy_img_arr.flatten()[j]
            noisy_img_arr.flatten()[i] = np.sign(activation)
    return noisy_img_arr.reshape(img_arr.shape)

# Limpiar la imagen ruidosa utilizando la red Hopfield
cleaned_img_arr = clean_image(noisy_img_arr, W)

# Mostrar las imágenes original, ruidosa y limpia
fig, axs = plt.subplots(1, 3, figsize=(15,5))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Imagen Original')
axs[1].imshow(noisy_img_arr, cmap='gray')
axs[1].set_title('Imagen Ruidosa')
axs[2].imshow(cleaned_img_arr, cmap='gray')
axs[2].set_title('Imagen Limpia')
plt.show()
