# @autor: Camilo Alejandro Areiza Mazo
# @fecha 12/10/2023
# @ficha: 2740559

# @Ejercicio: Escribir un ciclo for que cuente hasta cinco. Cuerpo del ciclo: imprimir el número de iteración el ciclo y La palabra 'Mississippi' Cuerpo del ciclo uso de la función time.sleep(1)
# @Ejercicio: Escribir una función de impresión con el mensaje final: listo o no, ahi voy!"

# import time

# def mensaje():
#     print("¡Listo o no, ahi voy!")

# for i in range(1, 6):
#     print(i)
#     print("Mississippi")
#     time.sleep(1)

# mensaje()



# @Ejercicio: generar e imprimir la serie de fibonacci para Los primeros 20 valores: 0, 1, 1, 2, 3, 5, 8, 13, ...

# f_anterior = 0
# f_despues = 1
# print(f" 1 : {f_anterior}/n2 :{f_despues} ")
# for i in range(2, 30):
#         f_siguiente = f_anterior + f_despues
#         print(f"{i + 1 :2d} : {f_siguiente:5d}")
#         f_anterior = f_despues
#         f_despues = f_siguiente

# @Ejercicio: 
#   generar un valor aleatorio entre 0 y 1000 para el numero secreto 
#   cuando se ingrese el numero se le debe dar una indicacion de si el numero
#   secreto esta por encima o por debajo del numero ingresado con la frase:
#   "el numero secreto es mayor" o "el numero secreto es menor"
#   el usuario va a tener 8 oportunidades para adivinar el numero
#   de lo contrario se terminara el proceso con la frase:
#   "lo siento muggle, no has adivinado el numero"

import random

def adivina_numero():
    numero = random.randint(0, 1000)
    intentos = 8
    print("+-------------------------------------------+")
    print("|                                           |")
    print("|   ¡Bienvenido a mi juego muggle!          |")
    print("|   introduce un numero entero y adivina    |")
    print("|   que numero he elegido para ti.          |")
    print("|   entonces,                               |")
    print("|   ¿cual es el numero secreto?             |")
    print("|                                           |")
    print("+-------------------------------------------+")
    
    while intentos > -1:
        intento = int(input("Ingresa un número entre 0 y 1000: "))
        print("----------------------------")
        print("Intentos restantes:", intentos)
        print("----------------------------")
        
        if intento == numero:
            print("¡Felicitaciones muggle! Has adivinado el número secreto")
            return
        
        elif intento < numero:
            print("El número secreto es mayor.")
            print("---------------------------")
        
        else:
            print("El número secreto es menor.")
            print("---------------------------")
        
        intentos -= 1
    
    print("Lo siento muggle, no has adivinado el número.")
    print("el numero secreto era:", numero)

adivina_numero()


# @Ejercicio: 
#   una vez un sombrero. el sombrero no contenia  conejo, sino 
#   una lista de cinco numeros: 1,2,3,4,5.
#   escribir un codigo que solicite al usuario que reemplace 
#   el numero central de esta lista con un numero entero ingresado por este
#   escribir una linea de codigo que elimine el ultimo elemento de la lista
#   escribir una linea de codigo que imprima la longitud de la lista existente 

# lista_numeros = [1, 2, 3, 4, 5]

# # Reemplaza el número central
# numero_ingresado = int(input("Ingresa un número entero: "))
# lista_numeros[2] = numero_ingresado

# # Elimina el último elemento de la lista
# del lista_numeros[-1]

# # Imprime la longitud de la lista
# print("Longitud de la lista:", len(lista_numeros))