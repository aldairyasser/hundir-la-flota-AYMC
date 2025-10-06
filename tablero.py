import numpy as np
from barco import barcos
from colocar_barcos import crea_barco_aleatorio, coloca_barco_plus

def tablero_vacio(lado = 10): # Creamos tablero vacío
    tablero = np.full((lado,lado),"_")
    return tablero # Devolvemos tablero

mi_tablero_barcos = tablero_vacio() # Creamos mi tablero vacio
tu_tablero_barcos = tablero_vacio() # Creamos tablero vacio de maquina

mi_tablero_disparos = tablero_vacio() # Creamos el tablero vacio de mis disparios
tu_tablero_disparo = tablero_vacio() #Creamos el tablero vacio de disparos de la maquina

for barco in barcos: # Metemos los barcos en mi tablero en función de su tamaño de barco
    mi_tablero_barcos = crea_barco_aleatorio(mi_tablero_barcos, barco)

for barco in barcos: # Metemos los barcos en tablero maquina en función del tamaño de barco
    tu_tablero_barcos = crea_barco_aleatorio(tu_tablero_barcos, barco)

#tu_tablero_barcos = crea_barco_aleatorio(tu_tablero_barcos, 2) #Tablero maquina con un barco de tamaño 2 Prueba de cierre ciclo si gano

#barco1 = [(0,1), (1,1)] #Prueba de cierre bucle si pierdo DISPARO1 DISPARO2

#barco2 = [(0,1)] #Prueba de cierre bucle si pierdo DISPARO1

#mi_tablero_barcos = coloca_barco_plus(mi_tablero_barcos ,barco1) #Prueba de cierre bucle si pierdo
