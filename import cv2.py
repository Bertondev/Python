import cv2

# Crea un objeto de captura de video
cap = cv2.VideoCapture(0)

# Comprueba si la cámara está funcionando correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

# Muestra la imagen de la cámara en una ventana
while True:
    # Lee la imagen de la cámara
    ret, frame = cap.read()

    # Comprueba si se pudo leer la imagen
    if not ret:
        print("No se pudo capturar la imagen")
        break

    # Muestra la imagen en una ventana
    cv2.imshow("Camara", frame)

    # Espera a que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) == ord('q'):
        break

# Libera los recursos utilizados por la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()


