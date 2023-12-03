#Crear el juego Tic, tac, toe(La vieja).

#Declaración de variables
tablero = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
player = "X"
ganador = None
juego = True

#Funcion para mostrar tablero
def imprimir_tablero(tablero):
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])


#Funcion para la entrada de datos del jugador.
def entrada_de_datos(tablero):
    posicion = int(input("Ingresar una posición del 1-9: "))
    if posicion >= 1 and posicion <= 9 and tablero[posicion - 1] == "-":
        tablero[posicion - 1] = player
    else:
        print("No papá, tas equivocado. Ya tu rival esta ocupando esta posición.😤")

#Chamo, esto es para que el algoritmo sepa cuando se gana el juego.

#En caso de que sea el mismo caracter en horizontal.
def checking_horizontal(tablero):
    global ganador
    if tablero[0] == tablero[1] == tablero[2] and tablero[1] != "-":
        ganador = tablero[0]
        return True
    elif tablero[3] == tablero[4] == tablero[5] and tablero[4] != "-":
        ganador = tablero[3]
        return True
    elif tablero[6] == tablero[7] == tablero[8] and tablero[7] != "-":
        ganador = tablero[6]
        return True

#En caso de que sea el mismo caracter en vertical.
def checking_vertical(tablero):
    global ganador
    if tablero[0] == tablero[3] == tablero[6] and tablero[3] != "-":
        ganador = tablero[0]
        return True
    elif tablero[1] == tablero[4] == tablero[7] and tablero[4] != "-":
        ganador = tablero[1]
        return True
    elif tablero[2] == tablero[5] == tablero[8] and tablero[5] != "-":
        ganador = tablero[2]
        return True

#En caso de que sea el mismo caracter en diagonal.
def checking_diagonal(tablero):
    global ganador
    if tablero[0] == tablero[4] == tablero[8] and tablero[4] != "-":
        ganador = tablero[0]
        return True
    elif tablero[2] == tablero[4] == tablero[6] and tablero[4] != "-":
        ganador = tablero[2]
        return True
    
#Esta funcion emite el mensaje pertinente cuando hay empate.
def checking_empate(tablero):
    global juego
    if "-" not in tablero:
        imprimir_tablero(tablero)
        print("Chamo, les gano la vieja.😲")
        juego = False

#Esta funcion emite el mensaje pertinente cuando hay un ganador.
def checking_ganador():
    global juego
    if checking_diagonal(tablero) or checking_vertical(tablero) or checking_horizontal(tablero):
        print(f"El jugador {ganador}, ha ganado.🤓")
        juego = False
 
#Cambio de jugador.
def cambio_jugador():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

#Ciclo while en el cual se llama a las funciones para correr el juego.
while juego:
    imprimir_tablero(tablero)
    entrada_de_datos(tablero)
    checking_ganador()
    checking_empate(tablero)
    cambio_jugador()