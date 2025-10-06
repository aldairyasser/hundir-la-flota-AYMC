from menu_juego import menu

print()
print("1. Sí")
print("0. NO")
print()

seguir = True

while seguir:
    try:
        decision = int(input("¿Quieres jugar a hundir la flota? (1/0): "))
        if decision == 1:
            menu() #Llamada al menú
            break
        else: #No quiere jugar
            print("Adios")
            seguir = False
    except:
        print("Elección no válida")

