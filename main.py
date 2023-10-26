# issues: Change Global board, don't place in done board, favorability
import copy
import board as gameState
import nextMove as computerThink

nextMoves = {}
board = "........."
totalBoard = ["", "", "", "", "", "", "", "", ""]
player = ""
computer = ""

for x in range(0, 9):
    totalBoard[x] = "........."

first = input("Who goes first (computer/player): ")
if (first == "computer"):
    player = "X"
    computer = "O"
else:
    player = "O"
    computer = "X"

goesNext = "X"
nextIndex = -1
while (("." in board) and (gameState.isFinished(board)[0] == False)):
    gameState.printBoard(board, totalBoard)
    print("")
    if (goesNext == player):
        print("computer's turn")
        temp = computerThink.maxMove(copy.copy(board), copy.copy(totalBoard), nextIndex, 3)
        board = temp[0]
        totalBoard = temp[1]
        nextIndex = temp[2]
        goesNext = computer
        print("")
    else:
        if (nextIndex == -1):
            nextIndex = int(input("Which board whould you like you like to play: "))
        print("your turn in board:", nextIndex)
        index = int(input("Where do you play (0-8): "))
        if (totalBoard[nextIndex][index] != "."):
            print("cant play there")
            print("")
            continue
        z = board.move(board, totalBoard, nextIndex, computer, index)
        board = z[0]
        totalBoard = z[1]
        nextIndex = z[2]
        goesNext = player
    print("_________________")
    print("")
board.printBoard(board, totalBoard)
x = board.isFinished(board)
if (x[1] == 0):
    print("draw")
if (x[1] == 1):
    print("X wins")
if (x[1] == -1):
    print("O wins")