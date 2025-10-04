from menu_juego import menu

print()
print("1. Sí")
print("0. NO")
print()

seguir = True

while seguir:
    try:
        desicion = int(input("¿Quieres jugar? (1/0): "))
        if desicion == 1:
            menu()
            break
        else:
            print("Adios")
            seguir = False
    except:
        print("Elección no válida")


