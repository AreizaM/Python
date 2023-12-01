# @ Autor: Camilo Alejandro Areiza Mazo
# @ Fecha: 17/10/2023
# @ Descripción: Defenición y ejecución de funciones 

# @Ejercicio: 
# Función: tarea pequeña, de varios renglones se utilizan para modulizar
# un sistema en partes más pequeñas de forma que se puedan modificar con facilidad, 
# y se puedan reconocer y corregir errores en el código.
# En algoritmia se llaman bubprocedimientos 
# En programación secuencial se llaman funciones o subrutinas
# En Poo: se llaman métodos o compartimientos 
# una función se reconoce de una variable porque tiene ().

# Tiene parametros: de entrada y de salida.
# Hay 4 tipos de funciones: 
# - sin parámetros de entrada -sin parámetro de salida.
# - sin parámetros de entrada -con parámetrso de salida.
# - con parámetros de entrada - sin parámetros de salida.
# - con parámetros de entrada - con parámetros de salida.

# Definición de una función en python: 
# Def Nombre_Función ([param1 [, param2, .....paramn]]):
# Cuerpo_de_la_función 
# [return valor]

# @Ejercicio: Crear una función para realizar la suma de dos números enteros.
# Primera forma: sin parámetros de entrada y sin parámetros de salida.

def sumar_forma_1():
    # Definir dos variables y capturar los datos por teclado
    op1 = int(input("Ingrese el primer número: "))
    op2 = int(input("Ingrese el segundo número: "))
    total = op1 + op2
    print(f"El resultado de {op1} + {op2} es {total}")

# Segunda forma: sin parámetros de entrada - con parámetro de salida.
def sumar_forma_2():
    # Definir dos variables y capturar los datos por teclado
    op1 = int(input("Ingrese el primer número: "))
    op2 = int(input("Ingrese el segundo número: "))
    total = op1 + op2
    return total

# Tercera forma: con parámetros de entrada - sin parámetros de salida.
def sumar_forma_3(op1, op2):
    total = op1 + op2
    print(f"El total de {op1} + {op2} es {total}")

# Cuarta forma: con parámetros de entrada - con parámetros de salida.
def sumar_forma_4(op1, op2):
    total = op1 + op2
    return total  # Retorna solo un parámetro

# Cuarta forma: con retorno de varios parámetros
def sumar_forma_42(op1, op2):
    total = op1 + op2
    return total, op1, op2

# Cuarta forma: con parámetros de entrada opcionales y un solo parámetro de salida
def sumar_forma_43(op1, op2 = 50):
    total = op1 + op2
    return total

# cuarta forma: con parametros de entrada opcionales varios parametros de salida

def sumar_forma_44(op1, op2 = 50):
    total = op1 + op2
    return total, op1, op2

# Programa principal
# Realizar la suma de los números utilizando funciones

print("Programa que realiza la suma de dos números")

# Utilizando la función ´sumar_forma_1()´
print("Utilizando la función ´sumar_forma_1´")
sumar_forma_1()

# Utilizando la función ´sumar_forma_2()´
print("Utilizando la función ´sumar_forma_2´")
total = sumar_forma_2()
print(f"El total es: {total}")

# Utilizando la función ´sumar_forma_3()´
# Primera forma
print("Utilizando la función ´sumar_forma_3´(param1, param2)")
sumar_forma_3(45, 35)

# Segunda forma
op1 = int(input("Ingrese el primer número: "))
op2 = int(input("Ingrese el segundo número: "))
sumar_forma_3(op1, op2)

# Utilizando la función ´sumar_forma_4(param1, param2)´
# Primera forma
total = sumar_forma_4(45, 38)
print(f"El total es: {total}")

# Segunda forma
op1 = int(input("Ingrese el primer número: "))
op2 = int(input("Ingrese el segundo número: "))
total2 = sumar_forma_4(op1, op2)
print(f"El total es: {total2}")

# Segunda forma de la segunda forma
print(f"El total es: {sumar_forma_4(op1, op2)}")

# Retorno de varios parámetros
print("Utilizando una función que retorna varios parámetros")
op1 = int(input("Ingrese el primer número: "))
op2 = int(input("Ingrese el segundo número: "))
total3, sumando1, sumando2 = sumar_forma_42(op1, op2)
print(f"La suma de: {sumando1} + {sumando2} es {total3}")

# Invocando una función con parámetro opcional
print("Utilizando una función con parámetro opcional")
op1 = int(input("Ingrese el primer número: "))
op2 = int(input("Ingrese el segundo número (opcional, presione Enter para usar el valor predeterminado): ") or 50)
total4 = sumar_forma_43(op1, op2)
print(f"El total es: {total4}")


# Invocando una función con parámetro opcional y con parametros de salida print("Utilizando una función con parámetro opcional")
print("""utilizando una funcion con parametro opcional y con varios parametros de salida""")
op1 = int(input("Ingrese el primer número: "))
op2 = int(input("Ingrese el segundo número (opcional, presione Enter para usar el valor predeterminado): "))

if op2 >= 0:
    total4, sumando1, sumando2 = sumar_forma_44(op1, op2)
else:
    total4, sumando1, sumando2 = sumar_forma_44(op1)

print(f"La suma de: {sumando1} + {sumando2} es {total4}")
