print("========Mi Super Calculadora==========")
num_1 = float(input("Escriba el valor del primer numero: "))
num_2 = float(input("Escriba el valor del segundo numero: "))
operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ")

def suma(num_1, num_2):
    return num_1 + num_2

if operacion == "+":
    resultado = suma(num_1, num_2)
    print("El resultado de la suma es: ", resultado)
    
    
def resta(num_1, num_2):
    return num_1 - num_2

if operacion == "-":
    resultado = resta(num_1, num_2)
    print("El resultado de la resta es: ", resultado)

def multilpicacion(num_1, num_2):
    return num_1 * num_2

if operacion == "*":
    resultado = suma(num_1, num_2)
    print("El resultado de la multiplicacion es: ", resultado)

def division(num_1, num_2):
    return num_1 / num_2

if operacion == "/":
    resultado = division(num_1, num_2)
    print("El resultado de la division es: ", resultado)