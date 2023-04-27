# Definir la función para sumar dos números
def suma(num1, num2):
    resultado = num1 + num2
    return resultado

# Definir la función para restar dos números
def resta(num1, num2):
    resultado = num1 - num2
    return resultado

# Definir la función para multiplicar dos números
def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

# Definir la función para dividir dos números
def division(num1, num2):
    # Manejar la división por cero
    if num2 == 0:
        print("¡Error! No puedes dividir entre cero.")
        return None
    else:
        resultado = num1 / num2
        return resultado

# Pedir al usuario que ingrese los números y la operación
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

# Realizar la operación correspondiente
if operacion == "+":
    resultado = suma(num1, num2)
elif operacion == "-":
    resultado = resta(num1, num2)
elif operacion == "*":
    resultado = multiplicacion(num1, num2)
elif operacion == "/":
    resultado = division(num1, num2)
else:
    print("Operación no válida. Por favor, ingresa una operación válida (+, -, *, /).")
    resultado = None

# Imprimir el resultado
if resultado is not None:
    print("El resultado es:", resultado)
