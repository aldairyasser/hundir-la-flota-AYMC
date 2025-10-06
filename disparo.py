from tablero import mi_tablero_disparos
import random

def recibir_disparo(tablero): # Función la cual usa la maquina para disparar en mi tablero barcos
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    coordenada = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1)) # El disparo es random en función a mi tablero
    if puedo_disparar(tablero):
        if tablero[coordenada] == "O":
            tablero[coordenada] = "X" # Si es parte de un barco que cambie la letra a "X" 
            return ("Tocado") # Y devuelve "Tocado"
        elif tablero[coordenada] == "A" or tablero[coordenada] == "X": # Si ya he disparado ahí
            return ("Agonia, deja de perder el tiempo, dispara a otro sitio") # Devuelve el mensaje
        else: 
            tablero[coordenada] = "A"
            return ("Agua") # Sino devuelve "Agua"

def disparar(tablero): # Función que usamos para disparar
    print("\nDime las coordenadas ") 
    x = int(input("Dame la posición x: ")) # Te pide coordenada x
    y = int(input("Dame la posición y: ")) # Te pide coordenadas y
    coordenada = (y,x) # Almacenamos coordenada
    if tablero[coordenada] == "O": 
        tablero[coordenada] = "X" # Si es parte de un barco que cambie la letra a "X" 
        mi_tablero_disparos[coordenada] = "X"
        return ("Tocado") # Y devuelve "Tocado"
    elif tablero[coordenada] == "A" or tablero[coordenada] == "X": # Si ya he disparado ahí
        return ("Agonia, deja de perder el tiempo, dispara a otro sitio") # Devuelve el mensaje
    else:
        tablero[coordenada] = "A"
        mi_tablero_disparos[coordenada] = "A"
        return ("Agua") # Sino devuelve "Agua"


def puedo_disparar(tablero): # Función que comprueba si se puede disparar
    if "O" in tablero:
        return True
    else:
        return False

def he_tocado(ataque): # Función que devulve si has Tocado o no
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


'''def disparo2(tablero): #Prueba cierre bucle si pierdo
    coordenada = (1,1)
    if puedo_disparar(tablero):
        if tablero[coordenada] == "O":
            tablero[coordenada] = "X"
            return ("Tocado")
        elif tablero[coordenada] == "A" or tablero[coordenada] == "X":
            return ("Agonia, deja de perder el tiempo, dispara a otro sitio")
        else:
            tablero[coordenada] = "A"
            return ("Agua")'''