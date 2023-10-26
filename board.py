NO_BOARD_VALUE = -1
IS_FINISHED_RESULT_X = 1
IS_FINISHED_RESULT_O = -1
IS_FINISHED_RESULT_DRAW = 0
IS_FINISHED_RESULT_NOT_FINISHED = 0
IS_FINISHED_RESULT_INDEX = 1
IS_FINISHED_OVER_YET_INDEX = 0

def printBoard(board, totalBoard):
    print("Board:")
    for row in range(0, 3):
        print(board[3 * row], board[3 * row + 1], board[3 * row + 2])
    print("")
    print("specific Boards:")
    for row in range(0, 3):
        for column in range(0, 3):
            print(totalBoard[3 * row][3 * column], totalBoard[3 * row][3 * column + 1], totalBoard[3 * row][3 * column + 2], "  ",
                  totalBoard[3 * row + 1][3 * column], totalBoard[3 * row + 1][3 * column + 1], totalBoard[3 * row + 1][3 * column + 2],
                  "  ", totalBoard[3 * row + 2][3 * column], totalBoard[3 * row + 2][3 * column + 1],
                  totalBoard[3 * row + 2][3 * column + 2])
        print("")


def isFinished(currentBoard):
    if (currentBoard[0] == 'X' and currentBoard[1] == 'X' and currentBoard[2] == 'X'):
        return (True, IS_FINISHED_RESULT_X)
    if (currentBoard[3] == 'X' and currentBoard[4] == 'X' and currentBoard[5] == 'X'):
        return (True, IS_FINISHED_RESULT_X)
    if (currentBoard[6] == 'X' and currentBoard[7] == 'X' and currentBoard[8] == 'X'):
        return (True, IS_FINISHED_RESULT_X)
    if (currentBoard[0] == 'X' and currentBoard[3] == 'X' and currentBoard[6] == 'X'):
        return (True, IS_FINISHED_RESULT_X)
    if (currentBoard[1] == 'X' and currentBoard[4] == 'X' and currentBoard[7] == 'X'):
        return (True, IS_FINISHED_RESULT_X)
    if (currentBoard[2] == 'X' and currentBoard[5] == 'X' and currentBoard[8] == 'X'):
        return (True, IS_FINISHED_RESULT_X)
    if (currentBoard[0] == 'X' and currentBoard[4] == 'X' and currentBoard[8] == 'X'):
        return (True, IS_FINISHED_RESULT_X)
    if (currentBoard[2] == 'X' and currentBoard[4] == 'X' and currentBoard[6] == 'X'):
        return (True, IS_FINISHED_RESULT_X)
    if (currentBoard[0] == 'O' and currentBoard[1] == 'O' and currentBoard[2] == 'O'):
        return (True, IS_FINISHED_RESULT_O)
    if (currentBoard[3] == 'O' and currentBoard[4] == 'O' and currentBoard[5] == 'O'):
        return (True, IS_FINISHED_RESULT_O)
    if (currentBoard[6] == 'O' and currentBoard[7] == 'O' and currentBoard[8] == 'O'):
        return (True, IS_FINISHED_RESULT_O)
    if (currentBoard[0] == 'O' and currentBoard[3] == 'O' and currentBoard[6] == 'O'):
        return (True, IS_FINISHED_RESULT_O)
    if (currentBoard[1] == 'O' and currentBoard[4] == 'O' and currentBoard[7] == 'O'):
        return (True, IS_FINISHED_RESULT_O)
    if (currentBoard[2] == 'O' and currentBoard[5] == 'O' and currentBoard[8] == 'O'):
        return (True, IS_FINISHED_RESULT_O)
    if (currentBoard[0] == 'O' and currentBoard[4] == 'O' and currentBoard[8] == 'O'):
        return (True, IS_FINISHED_RESULT_O)
    if (currentBoard[2] == 'O' and currentBoard[4] == 'O' and currentBoard[6] == 'O'):
        return (True, IS_FINISHED_RESULT_O)
    if ("." not in currentBoard):
        return (True, IS_FINISHED_RESULT_DRAW)
    return (False, IS_FINISHED_RESULT_NOT_FINISHED)

def possibleMoves(currentTotalBoard, position):
    moves = []
    for i in range(0, 9):
        if (currentTotalBoard[position][i] == "."):
            moves.append(i)
    return moves

def move(currentBoard, currentTotalBoard, boardPos, color, index):
    currentTotalBoard[boardPos] = currentTotalBoard[boardPos][0:index] + color + currentTotalBoard[boardPos][index + 1:]
    finished = isFinished(currentTotalBoard[boardPos])
    if (finished[IS_FINISHED_OVER_YET_INDEX]):
        currentBoard = currentBoard[0:boardPos] + color + currentBoard[boardPos + 1:]
    if (currentBoard[index] == "."):
        return (currentBoard, currentTotalBoard, index)
    else:
        return (currentBoard, currentTotalBoard, NO_BOARD_VALUE)

