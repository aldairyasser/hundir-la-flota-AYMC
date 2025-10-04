from tablero import mi_tablero_barcos, tu_tablero_barcos, mi_tablero_disparos 
from disparo import recibir_disparo, disparar, puedo_disparar, he_tocado, disparo1, disparo2
import time

# FILA, COLUMNA


def menu():
    seguir = True

    while seguir:
        time.sleep(0.5)
        print("\n--- MENÚ HUNDIR LA FLOTA ---")
        print("1. Mostar tu tablero")
        print("2. Mostrar tablero maquina (MODO DIOS)")
        print("3. Disparar")
        print("0. Salir")
        try:
            opcion = int(input("\nSelecciona un Nº tu elección: "))
            if opcion == 1:
                #Mostrar mi tablero
                print("\nMostrar mi tablero")
                print()
                print(mi_tablero_barcos)

            elif opcion == 2:
                #Mostrar tablero maquina
                print("\nMostrar tablero maquina")
                print()
                print(tu_tablero_barcos)

            elif opcion == 3:
                #Disparo
                if puedo_disparar(tu_tablero_barcos):
                    print()
                    print(mi_tablero_disparos)
                    mi_ataque = disparar(tu_tablero_barcos)
                    print()
                    time.sleep(1)
                    print(mi_ataque)
                    time.sleep(1)
                    if puedo_disparar(tu_tablero_barcos):
                        if not he_tocado(mi_ataque):
                            if puedo_disparar(mi_tablero_barcos):
                                print("\nTURNO DE LA MAQUINA")
                                ataque_maquina = recibir_disparo(mi_tablero_barcos)
                                print()
                                time.sleep(1)
                                print(ataque_maquina)
                                while ataque_maquina == "Tocado":
                                    if puedo_disparar(mi_tablero_barcos):
                                        time.sleep(1)
                                        print("\nTURNO DE LA MAQUINA")
                                        print()
                                        ataque_maquina = recibir_disparo(mi_tablero_barcos)
                                        time.sleep(1)
                                        print(ataque_maquina)
                                    else:
                                        print("\nNo te quedan barcos.")
                                        print("FIN DE LA PARTIDA")
                                        print("PERDISTE")
                                        break
                                break
                            else:
                                print("\nNo te quedan barcos.")
                                print("FIN DE LA PARTIDA")
                                print("PERDISTE")
                                break
                        else:
                            if puedo_disparar(tu_tablero_barcos):
                                print("\nTE VUELVE A TOCAR, DECIDE SABIAMENTE")
                                time.sleep(0.3)
                                continue
                            else:
                                print("\nNo le quedan barcos.")
                                print("FIN DE LA PARTIDA")
                                print("GANASTE")
                                break
                    else:
                        print("\nNo le quedan barcos.")
                        print("FIN DE LA PARTIDA")
                        print("GANASTE")
                        break
                else:
                    print("\nNo le quedan barcos.")
                    print("FIN DE LA PARTIDA")
                    print("GANASTE")
                    break
            elif opcion == 0:
                #ADIOS
                print()
                print("Adiós")
                seguir = False
            else:
                print(f"{opcion} opción no válida, volver a intentar.")
        except ValueError:
            print("Entrada no válida, debes ingresar un número.")
            print()

