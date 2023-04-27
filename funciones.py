#def imprimir_mensajes():
#    print('Mensaje especial: ')
# print('¡Estoy aprendiendo a usar funciones! ')


# imprimir_mensajes()
# imprimir_mensajes()
# imprimir_mensajes()

# def nombredelafuncion():
    # instrucciones de la función
def conversacion(opcion):
    print('Hola')
    print('Cómo estás')
    print('Elegiste la opcion: ' + str(opcion))
    print('Adiós')

opcion = int(input('Ingrese una opción (1, 2, 3): '))

if opcion == 1:
    conversacion(opcion)

elif opcion == 2:
    conversacion(opcion)

elif opcion == 3:
    conversacion(opcion)

else:
    print('Escribe una opción correcta.')
