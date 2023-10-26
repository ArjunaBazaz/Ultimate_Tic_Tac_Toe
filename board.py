def printBoard(board, totalBoard):
    print("Board:")
    for x in range(0, 3):
        print(board[3 * x], board[3 * x + 1], board[3 * x + 2])
    print("")
    print("specific Boards:")
    for x in range(0, 3):
        for y in range(0, 3):
            print(totalBoard[3 * x][3 * y], totalBoard[3 * x][3 * y + 1], totalBoard[3 * x][3 * y + 2], "  ",
                  totalBoard[3 * x + 1][3 * y], totalBoard[3 * x + 1][3 * y + 1], totalBoard[3 * x + 1][3 * y + 2],
                  "  ", totalBoard[3 * x + 2][3 * y], totalBoard[3 * x + 2][3 * y + 1],
                  totalBoard[3 * x + 2][3 * y + 2])
        print("")


def isFinished(currentBoard):
    if (currentBoard[0] == 'X' and currentBoard[1] == 'X' and currentBoard[2] == 'X'):
        return (True, 1)
    if (currentBoard[3] == 'X' and currentBoard[4] == 'X' and currentBoard[5] == 'X'):
        return (True, 1)
    if (currentBoard[6] == 'X' and currentBoard[7] == 'X' and currentBoard[8] == 'X'):
        return (True, 1)
    if (currentBoard[0] == 'X' and currentBoard[3] == 'X' and currentBoard[6] == 'X'):
        return (True, 1)
    if (currentBoard[1] == 'X' and currentBoard[4] == 'X' and currentBoard[7] == 'X'):
        return (True, 1)
    if (currentBoard[2] == 'X' and currentBoard[5] == 'X' and currentBoard[8] == 'X'):
        return (True, 1)
    if (currentBoard[0] == 'X' and currentBoard[4] == 'X' and currentBoard[8] == 'X'):
        return (True, 1)
    if (currentBoard[2] == 'X' and currentBoard[4] == 'X' and currentBoard[6] == 'X'):
        return (True, 1)
    if (currentBoard[0] == 'O' and currentBoard[1] == 'O' and currentBoard[2] == 'O'):
        return (True, -1)
    if (currentBoard[3] == 'O' and currentBoard[4] == 'O' and currentBoard[5] == 'O'):
        return (True, -1)
    if (currentBoard[6] == 'O' and currentBoard[7] == 'O' and currentBoard[8] == 'O'):
        return (True, -1)
    if (currentBoard[0] == 'O' and currentBoard[3] == 'O' and currentBoard[6] == 'O'):
        return (True, -1)
    if (currentBoard[1] == 'O' and currentBoard[4] == 'O' and currentBoard[7] == 'O'):
        return (True, -1)
    if (currentBoard[2] == 'O' and currentBoard[5] == 'O' and currentBoard[8] == 'O'):
        return (True, -1)
    if (currentBoard[0] == 'O' and currentBoard[4] == 'O' and currentBoard[8] == 'O'):
        return (True, -1)
    if (currentBoard[2] == 'O' and currentBoard[4] == 'O' and currentBoard[6] == 'O'):
        return (True, -1)
    if ("." not in currentBoard):
        return (True, 0)
    return (False, 0)


def move(currentBoard, currentTotalBoard, boardPos, color, index):
    currentTotalBoard[boardPos] = currentTotalBoard[boardPos][0:index] + color + currentTotalBoard[boardPos][index + 1:]
    x = isFinished(currentTotalBoard[boardPos])
    if (x[0] == True):
        currentBoard = currentBoard[0:boardPos] + color + currentBoard[boardPos + 1:]
    if (currentBoard[index] == "."):
        return (currentBoard, currentTotalBoard, index)
    else:
        return (currentBoard, currentTotalBoard, -1)


def possibleMoves(currentTotalBoard, position):
    moves = []
    for i in range(0, 9):
        if (currentTotalBoard[position][i] == "."):
            moves.append(i)
    return moves