### Esto es un comentario
### print('Hola mundo');
##
### @autor: Camilo Alejandro Areiza Mazo
### @fecha: 2023/10/05
### @descripcion: Ejercicios en Python
### @ => Significa anotaciones
##
### import keyword
##
### print("Hola Mundo de Python desde IDLE...")
### print("palabras reservadas de Python:", keyword.kwlisht)
##
### Definir una variable 'x' con el valor de la raíz cubica de 27
### x = 27 ** (1/3);
### print(f'Raíz de 27 es {x}');
##
###Ejercicio
###Resolver la ecuación 3x^3 - 2x^2 + 5x - 3
##
### x = 0
##
##x = 0;
##
##e = 3*(x**3) - 2*(x**2) + 5*x -3;
##
##print(e);
##
### x = 1
##x = 1;
##
##e = 3*(x**3) - 2*(x**2) + 5*x -3;
##
##print(e);
##
### x = -1
##x = -1;
##
##e = 3*(x**3) - 2*(x**2) + 5*x -3;
##
##print(e);
##
### x = 100
##x = 100;
##
##e = 3*(x**3) - 2*(x**2) + 5*x -3;
##
##print(e);

### Crear una credencial de presentación con los siguientes datos:
### 1- Nombres y apellidos
### 2- Número teléfonico
### 3- Redes sociales
##nombre = "Alejandro Areiza";
##telefono = 3135877374;
##instagram = "@ZieraK_";
##correo = "areizaplayer@gmail.com";
##print(f'#################################################\n',
##      f'#Hola mundo, mi nombre es {nombre}.     #\n',
##      f'#Mi número teléfonico es {telefono}             #\n',
##      f'#Instagram: {instagram}                            #\n',
##      f'#Correo: {correo}                 #\n',
##      f'#################################################');

### Calcular la hipotenusa de un triangulo rectángulo de lados 3 y 4 respectivamente
##hipotenusa = 3**2 + 4**2;
##print(hipotenusa);

### Realizar la conversión de pesos Colombianos a dólares, euros y viceversa a la tasa de cambio real
##pesoUsd = 4382;
##pesoEuro = 4612;
##pesoCop = int(input("Peso colombiano: "));
##
##convertCopToUsd = pesoCop/pesoUsd;
##convertCopToEuro = pesoCop/pesoEuro;
##
##print(f'COP:{pesoCop}\n',
##      f'USD:{convertCopToUsd}\n',
##      f'EURO:{convertCopToEuro}');

### Un automovil viaja a una velocidad de 120km/h, calcula la velocidad en m/h, km/s, m/s, mi/h y mi/s.
### ¿Cuál será la distancia recorrida si el automóvil viaja a esa misma velocidad durante 3,5 horas?
### Calcular la distancia en m, km, y mi.
##segundos = ((3.5 * 60)*60);
##
##velocidadKmSegundos = 120 / segundos;
##print(f'Kilometros por segundos:{velocidadKmSegundos:.4f} km/s\n');
##
##velocidadMHora = 120*1000 / (3.5 * 60);
##velocidadMSegundos = 120*1000 / segundos;
##print(f'Metros por hora: {velocidadMHora:.1f} m/h\n',
##      f'Metros por segundos:{velocidadMSegundos:.2f} m/s\n');
##
##velocidadMiHora = 120*0.621371 / (3.5 * 60);
##velocidadMiSegundos = 120*0.621371 / segundos;
##print(f'Millas por hora: {velocidadMiHora:.1f} mi/h\n',
##      f'Millas por segundos:{velocidadMiSegundos:.2f} mi/s\n');


### function input();
##cadena = input('Hola papasito, escribeme algo: ');
##print(f'Mensaje que ingreso el usuario: {cadena}');
##

##tipo_id = input('Tipo de documento de identidad: ');
##num_id = int(input('Número de documento de identidad: '));
##nombres = input('Nombres: ');
##apellidos = input("Apellidos: ")
##fecha_nacimiento = input("Fecha de nacimiento: ")
##edad = int(input ("Edad: "))
##correo = input("Correo:")
##print(f"""\n\t
##       ###############################################
##       #Tipo de identificacion: {tipo_id:9s}            #
##       #Numero de identificacion: {num_id:3d}       #
##       #Nombres: {nombres}                          #
##       #Apellidos: {apellidos:5s}                       #
##       #Fecha nacimiento: {fecha_nacimiento:18s}         #
##       #Edad: {edad:6d}                                 #
##       #Correo: {correo}               #
##       ###############################################
##        """)

##from tabulate import tabulate
##
##d = [tipo_id, num_id, nombres, apellidos, fecha_nacimiento,edad, correo]
##
##print(tabulate(d, headers=["Tipo de identificación",
##                           "Número de identificación",
##                           "Nombres",
##                           "Apellidos",
##                           "Fecha de nacimiento",
##                           "Edad",
##                           "Correo"]));
             
