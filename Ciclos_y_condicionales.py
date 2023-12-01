# @autor: Camilo Alejandro Areiza Mazo
# @fecha 10/10/2023
# @decripción: Ciclos y condicionales

# 324 ¿como identificar el mayor de dos numeros?
# los numeros deben ser ingresados por teclado y los numeros deben ser enteros


#leer numeros

# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))

# if num1 > num2:
#    mayor = num1
#    numeros = "numero1"
# else:
#    mayor = num2
#    numeros = "numero2"

# print(f"El numero mayor es {mayor} y es de la variable {numeros}")



# @Ejercicio: como identificar el mayor, el numero menor y el promedio de una secuencia de numeros?
#los numeros deben ser ingresados por teclado y los numeros enteros


# almacenamos el numero mas grande actual
mayor = -999999
menor = 999999  # Inicializar con un valor infinito para asegurarse de que cualquier número ingresado sea menor
contador_numeros = 0
suma = 0

# Ingresar el primer valor
print("Programa que encuentra el numero mayor, menor y el promedio de una secuencia de numeros")
print("Para terminar el programa, ingrese -1")

numero = int(input("Introduzca un numero o ingrese -1 para terminar: "))

# Si el numero no es igual a -1, continuaremos
while numero != -1:
    # Incrementar el contador y la suma de los numeros
    contador_numeros += 1
    suma += numero
    # Actualizar el numero mayor
    if numero > mayor:
        mayor = numero
    # Actualizar el numero menor
    if numero < menor:
        menor = numero
    # Solicitar un nuevo numero
    numero = int(input("Introduzca un numero o ingrese -1 para terminar: "))
# Calcular el promedio
if contador_numeros > 0:
    promedio = suma / contador_numeros
else:
    promedio = 0
# Imprimir el resultado
print(f"El numero mayor ingresado es: {mayor}")
print(f"El numero menor ingresado es: {menor}")
print(f"El promedio de los numeros ingresados es: {promedio} de un total de {contador_numeros} valores ingresados")



# empleados = []

# #solicita los datos de cada empleado
# while True:
#     print("\n Ingrese los datos del empleado:")
#     identificacion = input("Identificación: ")
#     nombres = input("Nombres: ")
#     apellidos = input("Apellidos: ")
#     correo = input("Correo: ")
#     salario_base = float(input("Salario base: "))

#     # Calcula las deducciones por salud y pensión
#     deducciones = salario_base * 0.04

#     # Calcula el salario neto
#     salario_neto = salario_base - deducciones

#     # Verifica si se aplica una comisión adicional
#     if salario_neto < 1000000:
#         comision = salario_base * 0.12
#         salario_neto += comision
#     else:
#         comision = 0

#     # Agrega los datos del empleado a la lista
#     empleado = {
#         "identificacion": identificacion,
#         "nombres": nombres + " " + apellidos,
#         "correo": correo,
#         "salario_base": salario_base,
#         "salud": deducciones,
#         "pension": deducciones,
#         "salario_neto": salario_neto,
#         "comision": comision
#     }
#     empleados.append(empleado)

#     # Preguntar si se desea ingresar otro empleado
#     respuesta = input("¿Desea ingresar otro empleado? (s/n): ")
#     if respuesta.lower() != 's':
#         break

# # Calcular el promedio de los diferentes valores
# num_empleados = len(empleados)
# promedio_salario_base = sum(empleado["salario_base"] for empleado in empleados) / num_empleados
# promedio_salud = sum(empleado["salud"] for empleado in empleados) / num_empleados
# promedio_pension = sum(empleado["pension"] for empleado in empleados) / num_empleados
# promedio_salario_neto = sum(empleado["salario_neto"] for empleado in empleados) / num_empleados
# promedio_comisiones = sum(empleado["comision"] for empleado in empleados) / num_empleados

# # Mostrar la información de cada empleado
# for i, empleado in enumerate(empleados):
#     print("\n--- Información del Empleado --------")
#     print(f"Empleado número: {i+1}")
#     print(f"Identificación: {empleado['identificacion']}")
#     print(f"Nombres: {empleado['nombres']}")
#     print(f"Correo: {empleado['correo']}")
#     print(f"Salario base: COP ${empleado['salario_base']}")
#     print(f"Salud: COP ${empleado['salud']}")
#     print(f"Pensión: COP ${empleado['pension']}")
#     print(f"Salario Neto: COP ${empleado['salario_neto']}")
#     print(f"Comisión: COP ${empleado['comision']}")
#     print("--------------------------------")

# # Imprimir los promedios
# print("\n--- Promedios ---")
# print(f"Promedio Salario Base: COP ${promedio_salario_base}")
# print(f"Promedio Salud: COP ${promedio_salud}")
# print(f"Promedio Pensión: COP ${promedio_pension}")
# print(f"Promedio Salario Neto: COP ${promedio_salario_neto}")
# print(f"Promedio Comisiones: COP ${promedio_comisiones}")
# print("-------------------------")
