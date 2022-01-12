from random import randrange

def DisplayBoard(board):
	print("+-------" * 3,"+",sep="")
	for fila in range(3):
		print("|       " * 3,"|",sep="")
		for columna in range(3):
			print("|   " + str(board[fila][columna]) + "   ",end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def EnterMove(board):
	esMovimientoPermitido = False
	while not esMovimientoPermitido:
		move = input("Elige una celda: ")
		esMovimientoPermitido = len(move) == 1 and move >= '1' and move <= '9'
		if not esMovimientoPermitido:
			print("Movimiento incorrecto, intenta otro")
			continue
		move = int(move) - 1
		fila = move // 3
		columna = move % 3
		sign = board[fila][columna]
		esMovimientoPermitido = sign not in ['O','X'] 
		if not esMovimientoPermitido:
			print("Esta celda ya esta ocupada, elige otra")
			continue
	board[fila][columna] = 'O'

def MakeListOfFreeFields(board):
	celdasLibres = []
	for fila in range(3):
		for columna in range(3):
			if board[fila][columna] not in ['O','X']:
				celdasLibres.append((fila,columna))
	return celdasLibres


def VictoryFor(board,sign):
	if sign == "X":
		ganador = 'computadora'
	elif sign == "O":
		ganador = 'jugador'
	else:
		ganador = None
    
	diagonal_1 = True
	diagonal_2 = True

	for rc in range(3):
		if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
			return ganador
		if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
			return ganador
		if board[rc][rc] != sign:
			diagonal_1 = False
		if board[2 - rc][2 - rc] != sign:
			diagonal_2 = False
	if diagonal_1 or diagonal_2:
		return ganador
	return None

def DrawMove(board):
	celdasLibres = MakeListOfFreeFields(board)
	numeroCeldasLibres = len(celdasLibres)
	if numeroCeldasLibres > 0:
		this = randrange(numeroCeldasLibres)
		fila, columna = celdasLibres[this]
		board[fila][columna] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
board[1][1] = 'X'
celdasLibres = MakeListOfFreeFields(board)
turnoJugador = True
while len(celdasLibres):
	DisplayBoard(board)
	if turnoJugador:
		EnterMove(board)
		victoria = VictoryFor(board,'O')
	else:	
		DrawMove(board)
		victoria = VictoryFor(board,'X')
	if victoria != None:
		break
	turnoJugador = not turnoJugador		
	celdasLibres = MakeListOfFreeFields(board)

DisplayBoard(board)
if victoria == 'jugador':
	print("¡Tu ganaste!")
elif victoria == 'computadora':
	print("¡Yo gano!")
else:
	print("¡Empate!")