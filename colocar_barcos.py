import random
import numpy as np

def coloca_barco_plus(tablero, barco): # Función que verifica que se pueda colocar barco en función al tamaño de tablero
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            return False
        if columna <0 or columna>= num_max_columnas:
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

def crea_barco_aleatorio(tablero,tamaño_barco = 2, num_intentos = 100): # Creamos la función para colocar un barcos de tamaño x de forma aleatorio en tablero
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        # Construimos el hipotetico barco
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"]) # Random de la dirección del barco
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(tamaño_barco -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco) # Llamar a la función de validación para comprobar si se puede poner el barco
        if type(tablero_temp) == np.ndarray:
            return tablero_temp # Devolvemos el tablero, si no volvermos a intertar con otras coordenadas
