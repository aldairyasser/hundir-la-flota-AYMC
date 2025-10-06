from tablero import mi_tablero_barcos, tu_tablero_barcos, mi_tablero_disparos 
from disparo import recibir_disparo, disparar, puedo_disparar, he_tocado#, disparo1, disparo2
import time

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
                # Mostrar mi tablero
                print("\nMostrar mi tablero")
                print()
                print(mi_tablero_barcos)

            elif opcion == 2:
                # Mostrar tablero maquina
                print("\nMostrar tablero maquina")
                print()
                print(tu_tablero_barcos)

            elif opcion == 3:
                # Disparo
                if puedo_disparar(tu_tablero_barcos):
                    print()
                    print(mi_tablero_disparos) # Mostrar tablera de mis disparos
                    mi_ataque = disparar(tu_tablero_barcos) # Llamar a la función dispara y almacenamos la salida
                    print()
                    time.sleep(1)
                    print(mi_ataque) #Mostrar el mensaje del disparo (Fallo o acierto)
                    time.sleep(1)
                    if puedo_disparar(tu_tablero_barcos): # Comprobar si puedo disparar (si a la maquina le quedan barcos)
                        if not he_tocado(mi_ataque): # Comprobar si he tocado, sino turno de maquina
                            if puedo_disparar(mi_tablero_barcos): # Comprobar si la maquina puede disparar (si me quedan barcos)
                                print("\nTURNO DE LA MAQUINA")
                                ataque_maquina = recibir_disparo(mi_tablero_barcos) # Llamamos a la función de ataque_maquina, para 
                                # ataque_maquina = disparo1(mi_tablero_barcos)
                                print()
                                time.sleep(1)
                                print(ataque_maquina)
                                while ataque_maquina == "Tocado": # Mientras que la maquina acierte
                                    if puedo_disparar(mi_tablero_barcos): # Comprobar de nuevo si la maquina puede disparar 
                                        time.sleep(1)
                                        print("\nTURNO DE LA MAQUINA")
                                        print()
                                        ataque_maquina = recibir_disparo(mi_tablero_barcos) # Almacenamos la salida del ataque de la maquina
                                        # ataque_maquina = disparo2(mi_tablero_barcos)
                                        time.sleep(1)
                                        print(ataque_maquina) # Mostramos el ataque de la maquina
                                    else: # Si no me quedan barcos se mete aquí
                                        print("\nNo te quedan barcos.")
                                        print("FIN DE LA PARTIDA")
                                        print("PERDISTE")
                                        break # Salimos del bucle while si no nos quedan barcos
                            else: # Se mete aquí si no me quedan barcos en la primera validadción
                                print("\nNo te quedan barcos.")
                                print("FIN DE LA PARTIDA")
                                print("PERDISTE")
                                break # Salimos del bucle
                        else: # Se mete aqui si he acertado
                            if puedo_disparar(tu_tablero_barcos): # Comprobamos si puedo disparar (Si le quedan barcos a la maquina)
                                print("\nTE VUELVE A TOCAR, DECIDE SABIAMENTE")
                                time.sleep(0.3)
                                continue # Mostramos menú de nuevo, por si acaso quiere salir.
                            else: # Se mete aquí si no le quedan barcos a la maquina 
                                print("\nNo le quedan barcos.")
                                print("FIN DE LA PARTIDA")
                                print("GANASTE")
                                break # Fin bucle
                    else: # Se mete aquí si no le quedan barcos a la maquina
                        print("\nNo le quedan barcos.")
                        print("FIN DE LA PARTIDA")
                        print("GANASTE")
                        break # Fin bucle while
                else: # Se mete aquí si no le quedan barcos a la maquina
                    print("\nNo le quedan barcos.")
                    print("FIN DE LA PARTIDA")
                    print("GANASTE")
                    break # Fin bucle while
            elif opcion == 0:
                #ADIOS
                print()
                print("Adiós")
                seguir = False # Cambiamos valor al while para salir
            else:
                print(f"{opcion} opción no válida, volver a intentar.")
        except ValueError:
            print("Entrada no válida, debes ingresar un número.")
            print()

