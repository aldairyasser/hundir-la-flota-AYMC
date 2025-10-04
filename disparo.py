from tablero import mi_tablero_disparos
import random

def recibir_disparo(tablero):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    coordenada = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
    if puedo_disparar(tablero):
        if tablero[coordenada] == "O":
            tablero[coordenada] = "X"
            return ("Tocado")
        elif tablero[coordenada] == "A" or tablero[coordenada] == "X":
            return ("Agonia, deja de perder el tiempo, dispara a otro sitio")
        else:
            tablero[coordenada] = "A"
            return ("Agua") 

def disparar(tablero):
    if puedo_disparar(tablero):
        print("\nDime las coordenadas ")
        x = int(input("Dame la posición x: "))
        y = int(input("Dame la posición y: "))
        coordenada = (y,x)
        if tablero[coordenada] == "O":
            tablero[coordenada] = "X"
            mi_tablero_disparos[coordenada] = "X"
            return ("Tocado")
        elif tablero[coordenada] == "A" or tablero[coordenada] == "X":
            return ("Agonia, deja de perder el tiempo, dispara a otro sitio")
        else:
            tablero[coordenada] = "A"
            mi_tablero_disparos[coordenada] = "A"
            return ("Agua")


def puedo_disparar(tablero):
    if "O" in tablero:
        return True
    else:
        return False

def he_tocado(ataque):
    if ataque == "Tocado":
        return True
    else:
        return False
    

'''def disparo1(tablero): #Prueba cierre bucle si pierdo
    coordenada = (0,1)
    if puedo_disparar(tablero):
        if tablero[coordenada] == "O":
            tablero[coordenada] = "X"
            return ("Tocado")
        elif tablero[coordenada] == "A" or tablero[coordenada] == "X":
            return ("Agonia, deja de perder el tiempo, dispara a otro sitio")
        else:
            tablero[coordenada] = "A"
            return ("Agua")'''


