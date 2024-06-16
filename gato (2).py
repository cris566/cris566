import random

Tablero = [' ' for _ in range(9)]

def print_Tablero(Tablero):
    linea1 = '| {} | {} | {} |'.format(Tablero[0], Tablero[1], Tablero[2])
    linea2 = '| {} | {} | {} |'.format(Tablero[3], Tablero[4], Tablero[5])
    linea3 = '| {} | {} | {} |'.format(Tablero[6], Tablero[7], Tablero[8])

    print()
    print(linea1)
    print(linea2)
    print(linea3)
    print()

def movimiento_Jugador(icono):
    if icono == 'X':
        number = 1
    elif icono == 'O':
        number = 2

    print("Turno del Jugador {}".format(number))
    eleccion = int(input("Coloca la coordenada de movimiento (1-9): ").strip())

    if Tablero[eleccion - 1] == ' ':
        Tablero[eleccion - 1] = icono
    else:
        print()
        print("Ese espacio ya está ocupado!")

def es_victoria(icono):
    return ((Tablero[0] == icono and Tablero[1] == icono and Tablero[2] == icono) or
            (Tablero[3] == icono and Tablero[4] == icono and Tablero[5] == icono) or
            (Tablero[6] == icono and Tablero[7] == icono and Tablero[8] == icono) or
            (Tablero[0] == icono and Tablero[3] == icono and Tablero[6] == icono) or
            (Tablero[1] == icono and Tablero[4] == icono and Tablero[7] == icono) or
            (Tablero[2] == icono and Tablero[5] == icono and Tablero[8] == icono) or
            (Tablero[0] == icono and Tablero[4] == icono and Tablero[8] == icono) or
            (Tablero[2] == icono and Tablero[4] == icono and Tablero[6] == icono))

while True:
    print("Menu de Gato")
    print("1. Jugador 1 vs COM")
    print("2. Jugador 1 vs Jugador 2")
    print("3. Salir")

    opc = input("Seleccione una opción (1-3): ")

    if opc == "1":
        # Implement Player vs COM logic
        Tablero = [' ' for _ in range(9)]
        game_on = True
        turn = 'Jugador 1'
        while game_on:
            if turn == 'Jugador 1':
                print_Tablero(Tablero)
                movimiento_Jugador('X')
                if es_victoria('X'):
                    print_Tablero(Tablero)
                    print('¡Felicidades! Jugador 1 gana!')
                    game_on = False
                elif ' ' not in Tablero:
                    print_Tablero(Tablero)
                    print('¡Es un empate!')
                    break
                else:
                    turn = 'COM'
            else:
                posicion = random.randint(1, 9)
                while Tablero[posicion - 1] != ' ':
                    posicion = random.randint(1, 9)
                Tablero[posicion - 1] = 'O'

                if es_victoria('O'):
                    print_Tablero(Tablero)
                    print('¡Felicidades! COM gana!')
                    game_on = False
                elif ' ' not in Tablero:
                    print_Tablero(Tablero)
                    print('¡Es un empate!')
                    break
                else:
                    turn = 'Jugador 1'

    elif opc == "2":
        # Implement Player vs Player logic
        Tablero = [' ' for _ in range(9)]
        while True:
            print_Tablero(Tablero)
            movimiento_Jugador('X')
            if es_victoria('X'):
                print("Jugador 1 gana! ¡Felicidades!")
                break
            elif ' ' not in Tablero:
                print("¡Es un empate!")
                break
            print_Tablero(Tablero)
            movimiento_Jugador('O')
            if es_victoria('O'):
                print_Tablero(Tablero)
                print("Jugador 2 gana! ¡Felicidades!")
                break

    elif opc == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")