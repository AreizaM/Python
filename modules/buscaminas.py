# @autor: Camilo Alejandro Areiza Mazo
# @fecha: 19/10/20023
# @descripción: Funciones para el backend y frontend del juego de buscaminas

# Importación de módulos
import math
import random
import os

# Valor de la mina
MINA = -1;

# Funciones del backend para el juego de buscaminas

# Crear tablero 
def crearTablero (filas, columnas, porcentajeMinas = 30):
    dibujarTablero = [[0 for j in range(columnas)]for i in range(filas)];
    insertarMinas(dibujarTablero, porcentajeMinas);
    conteoMinas(dibujarTablero);
    return dibujarTablero; 

# Inserción de minas
def insertarMinas(tablero, porcentajeMinas):
    # Definición de contador
    contadorMinas = 0;
    # Calcular el número de minas en el tablero
    filas = len(tablero);
    columnas = len(tablero[0]);
    minas = math.ceil(filas * columnas * (porcentajeMinas / 100));
    
    # Elección de una fila y una columna al azar
    while contadorMinas < minas:
        fila = random.randrange(0, filas);
        columna = random.randrange(0, columnas);
        
        # Validar de minas 
        if tablero[fila][columna] != MINA:
            tablero[fila][columna] = MINA;
            contadorMinas += 1;
        else:
            continue

# Constructor de funciones
def conteoMinas(tablero):
    conteoMinasExtremoSuperior(tablero);
    conteoMinasLateralIzquierdo(tablero);
    conteoMinasCentral(tablero);
    conteoMinasLateralDerecho(tablero);
    conteoMinasExtremoInferior(tablero);
    conteoMinasInferiorDerecha(tablero);
    conteoMinasInferiorIzquierda(tablero);
    conteoMinasSuperiorDerecha(tablero);
    conteoMinasSuperiorIzquierda(tablero);


# Conteo de minas alrededor de cada una de las celdas
def conteoMinasCentral(tablero):
    # Recorrer el tablero por índice
    filas = len(tablero);
    columnas = len(tablero[0]);
    for i in range(1, filas -1):
        for j in range(1, columnas - 1):
            if tablero[i][j] != MINA:
                if tablero[i-1][j-1] == MINA:
                    tablero[i][j] += 1;
                if tablero[i-1][j] == MINA:
                    tablero[i][j] += 1;
                if tablero[i-1][j+1] == MINA:
                    tablero[i][j] += 1;
                if tablero[i][j-1] == MINA:
                    tablero[i][j] += 1;
                if tablero[i][j+1] == MINA:
                    tablero[i][j] += 1;
                if tablero[i+1][j-1] == MINA:
                    tablero[i][j] += 1;
                if tablero[i+1][j] == MINA:
                    tablero[i][j] += 1;
                if tablero[i+1][j+1] == MINA:
                    tablero[i][j] += 1;


# Conteo de minas alrededor de el lateral izquierdo
def conteoMinasLateralIzquierdo(tablero):
    filas = len(tablero);
    for i in range(1, filas -1):
            if tablero[i][0] != MINA:
                if tablero[i-1][0] == MINA:
                    tablero[i][0] += 1;
                if tablero[i-1][1] == MINA: 
                    tablero[i][0] += 1;
                if tablero[i][1] == MINA: 
                    tablero[i][0] += 1;
                if tablero[i+1][0] == MINA: 
                    tablero[i][0] += 1;
                if tablero[i+1][1] == MINA: 
                    tablero[i][0] += 1;


# Conteo de minas alrededor de el lateral derecho
def conteoMinasLateralDerecho(tablero):
    filas = len(tablero);
    for i in range(1, filas -1):
            if tablero[i][-1] != MINA:
                if tablero[i-1][-1] == MINA:
                    tablero[i][-1] += 1;
                if tablero[i-1][-2] == MINA: 
                    tablero[i][-1] += 1;
                if tablero[i][-2] == MINA: 
                    tablero[i][-1] += 1;
                if tablero[i+1][-1] == MINA: 
                    tablero[i][-1] += 1;
                if tablero[i+1][-2] == MINA: 
                    tablero[i][-1] += 1;

# Conteo de minas alrededor del extremo superior
def conteoMinasExtremoSuperior(tablero):
    columnas = len(tablero[0]);
    for j in range(1, columnas -1):
            if tablero[0][j] != MINA:
                if tablero[0][j-1] == MINA:
                    tablero[0][j] += 1;
                if tablero[0][j+1] == MINA:
                    tablero[0][j] += 1;
                if tablero[1][j-1] == MINA:
                    tablero[0][j] += 1;
                if tablero[1][j] == MINA:
                    tablero[0][j] += 1;
                if tablero[1][j+1] == MINA:
                    tablero[0][j] += 1;
                

# Conteo de minas alrededor del extremo inferior
def conteoMinasExtremoInferior(tablero):
    columnas = len(tablero[0]);
    for j in range(1, columnas -1):
            if tablero[-1][j] != MINA:
                if tablero[-1][j-1] == MINA:
                    tablero[-1][j] += 1;
                if tablero[-1][j+1] == MINA:
                    tablero[-1][j] += 1;
                if tablero[-2][j-1] == MINA:
                    tablero[-1][j] += 1;
                if tablero[-2][j] == MINA:
                    tablero[-1][j] += 1;
                if tablero[-2][j+1] == MINA:
                    tablero[-1][j] += 1;


# Conteo de minas alrededor de la esquina superior izquierda
def conteoMinasSuperiorIzquierda(tablero):
        if tablero[0][0] != MINA:
                if tablero[0][1] == MINA:
                    tablero[0][0] += 1;
                if tablero[1][0] == MINA:
                    tablero[0][0] += 1;
                if tablero[1][1] == MINA:
                    tablero[0][0] += 1;


# Conteo de minas alrededor de la esquina superior derecha
def conteoMinasSuperiorDerecha(tablero):
        if tablero[0][-1] != MINA:
                if tablero[0][-2] == MINA:
                    tablero[0][-1] += 1;
                if tablero[1][-1] == MINA:
                    tablero[0][-1] += 1;
                if tablero[1][-2] == MINA:
                    tablero[0][-1] += 1;


# Conteo de minas alrededor de la esquina inferior izquierda
def conteoMinasInferiorIzquierda(tablero):
    if tablero[-1][0] != MINA:
        if tablero[-2][0] == MINA:
            tablero[-1][0] += 1;
        if tablero[-2][1] == MINA:
            tablero[-1][0] += 1;
        if tablero[-1][1] == MINA:
            tablero[-1][0] += 1;


# Conteo de minas alrededor de la esquina inferior derecha
def conteoMinasInferiorDerecha(tablero):
        if tablero[-1][-1] != MINA:
                if tablero[-2][-1] == MINA:
                    tablero[-1][-1] += 1;
                if tablero[-2][-2] == MINA:
                    tablero[-1][-1] += 1;
                if tablero[-1][-2] == MINA:
                    tablero[-1][-1] += 1;


