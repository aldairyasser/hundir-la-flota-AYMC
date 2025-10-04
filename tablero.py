import numpy as np
from barco import barcos
from colocar_barcos import crea_barco_aleatorio, coloca_barco_plus

def tablero_vacio(lado = 10):
    tablero = np.full((lado,lado),"_")
    return tablero

mi_tablero_barcos = tablero_vacio()
tu_tablero_barcos = tablero_vacio()

mi_tablero_disparos = tablero_vacio()
tu_tablero_disparo = tablero_vacio()

for barco in barcos:
    mi_tablero_barcos = crea_barco_aleatorio(mi_tablero_barcos, barco)

for barco in barcos:
    tu_tablero_barcos = crea_barco_aleatorio(tu_tablero_barcos, barco)

#tu_tablero_barcos = crea_barco_aleatorio(tu_tablero_barcos, 2) #Tablero maquina con un barco de tamaño 2 Prueba de cierre ciclo si gano

#barco1 = [(0,1)] #Prueba de cierre bucle si pierdo

#mi_tablero_barcos = coloca_barco_plus(mi_tablero_barcos ,barco1) #Prueba de cierre bucle si pierdo
