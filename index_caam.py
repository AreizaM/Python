# @autor: Camilo Alejandro Areiza Mazo
# @fecha: 19/10/20023
# @descripción: Programa principal para el juego de buscaminas.

# Llamada de módulo
from modules import buscaminas as bm

# Mensaje por consola
print('¡Bem-vindo ao jogo de buscaminas pelo console!');

# Inserción de datos
nFilas = int(input('Ingrese el número de filas del tablero: '));
nColumnas = int(input('Ingrese el número de columnas del tablero: '));

# Creación del tablero
tablero = bm.crearTablero(nFilas, nColumnas);

# Recorrido del tablero
for i in range(nFilas):
    print("[", end=' ');
    for j in range(nColumnas):
        if j == nColumnas-1:
            print(f"{tablero[i][j]:2d}", end=" ");
        else:
            print(f"{tablero[i][j]:2d}", end=", " );
    print(' ]');

