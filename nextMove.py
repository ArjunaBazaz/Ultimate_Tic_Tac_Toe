import copy
import board as board

def scoreBoard(currentBoard):
    XScore = 0
    OScore = 0
    z = board.isFinished(currentBoard)
    if (z[0] == True):
        return 20 * z[1]
    for x in range(0, 9):
        if (currentBoard[x] == 'X'):
            XScore = XScore + 2
        elif (currentBoard[x] == 'O'):
            OScore = OScore + 2
        else:
            tempBoard = currentBoard[0:x] + "X" + currentBoard[x + 1:]
            if (board.isFinished(tempBoard)[0]):
                XScore = XScore + 4
            tempBoard = currentBoard[0:x] + "O" + currentBoard[x + 1:]
            if (board.isFinished(tempBoard)[0]):
                OScore = OScore + 4
        if (x == 4):
            if (currentBoard[x] == 'X'):
                XScore = XScore + 1
            elif (currentBoard[x] == 'O'):
                OScore = OScore + 1
    return XScore - OScore


def favorability2(currentBoard, currentTotalBoard):
    XScore = 0
    OScore = 0
    totalScore = 0
    indicies = {}
    z = board.isFinished(currentBoard)
    if (z[0] == True):
        return 1000 * z[1]
    for x in range(0, 9):
        indicies[x] = scoreBoard(currentTotalBoard[x])
    for x in range(0, 9):
        totalScore = totalScore + indicies[x]
    return totalScore + XScore - OScore


def favorability(currentBoard, currentTotalBoard):  # FINISH FAVORABILITY
    XScore = 0
    OScore = 0
    totalScore = 0
    z = board.isFinished(currentBoard)
    if (z[0] == True):
        return 1000 * z[1]
    for x in range(0, 9):
        if (currentBoard[x] == 'X'):
            XScore = XScore + 40
            if (x % 3 < 2 and currentBoard[x + 1] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 1])
            elif (x % 3 != 0 and currentBoard[x - 1] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 1])
            elif (x < 6 and currentBoard[x + 3] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 3])
            elif (x > 2 and currentBoard[x - 3] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 3])
            elif (x % 3 < 2 and x < 6 and currentBoard[x + 4] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 4])
            elif (x % 3 != 0 and x > 2 and currentBoard[x - 4] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 4])
            elif (x % 3 != 0 and x < 6 and currentBoard[x + 2] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 2])
            elif (x % 3 < 2 and x > 2 and currentBoard[x - 2] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 2])
        elif (currentBoard[x] == 'O'):
            OScore = OScore + 40
            if (x % 3 < 2 and currentBoard[x + 1] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 1])
            elif (x % 3 != 0 and currentBoard[x - 1] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 1])
            elif (x < 6 and currentBoard[x + 3] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 3])
            elif (x > 2 and currentBoard[x - 3] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 3])
            elif (x % 3 < 2 and x < 6 and currentBoard[x + 4] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 4])
            elif (x % 3 != 0 and x > 2 and currentBoard[x - 4] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 4])
            elif (x % 3 != 0 and x < 6 and currentBoard[x + 2] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 2])
            elif (x % 3 < 2 and x > 2 and currentBoard[x - 2] == "."):
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 2])
        else:
            tempBoard = currentBoard[0:x] + "X" + currentBoard[x + 1:]
            if (board.isFinished(tempBoard)[0]):
                XScore = XScore + 100
                totalScore = totalScore + 4 * scoreBoard(currentTotalBoard[x])
            tempBoard = currentBoard[0:x] + "O" + currentBoard[x + 1:]
            if (board.isFinished(tempBoard)[0]):
                OScore = OScore + 100
                totalScore = totalScore + 4 * scoreBoard(currentTotalBoard[x])
            totalScore = totalScore + scoreBoard(currentTotalBoard[x])
        if (x == 0 or x == 2 or x == 6 or x == 8):
            if (currentBoard[x] == 'X'):
                XScore = XScore + 10
            elif (currentBoard[x] == 'O'):
                OScore = OScore + 10
            else:
                totalScore = totalScore + scoreBoard(currentTotalBoard[x])
        if (x == 4):
            if (currentBoard[x] == 'X'):
                XScore = XScore + 25
            elif (currentBoard[x] == 'O'):
                OScore = OScore + 25
            else:
                totalScore = totalScore + 2 * scoreBoard(currentTotalBoard[x])
    return totalScore + XScore - OScore


def max_step(currentBoard, currentTotalBoard, position, depth, alpha, beta, player):  # Whatif no moves available
    f = board.isFinished(currentBoard)
    results = []
    if (depth == 0 or f[0] == True):
        if (player == "X"):
            return favorability(copy.copy(currentBoard), currentTotalBoard)
        else:
            return (-1) * favorability(copy.copy(currentBoard), currentTotalBoard)
    moves = []
    if (position == -1):
        for x in range(0, 9):
            if (currentBoard[x] == "."):
                for y in board.possibleMoves(currentTotalBoard, x):
                    moves.append((y, x))
    else:
        for y in board.possibleMoves(currentTotalBoard, position):
            moves.append((y, position))
    if (len(moves) == 0):
        return min_step(copy.copy(currentBoard), copy.copy(currentTotalBoard), -1, depth - 1, alpha, beta, player)
    for nextIndex in moves:
        toMove = board.move(copy.copy(currentBoard), copy.copy(currentTotalBoard), nextIndex[1], player, nextIndex[0])
        z = min_step(toMove[0], toMove[1], toMove[2], depth - 1, alpha, beta, player)
        results.append(z)
        if (z > alpha):
            alpha = z
        if (beta <= alpha):  # pruning
            break
    if (len(results) != 0):
        return max(results)


def min_step(currentBoard, currentTotalBoard, position, depth, alpha, beta, player):
    f = board.isFinished(currentBoard)
    results = []
    if (depth == 0 or f[0] == True):
        if (player == "X"):
            return favorability(copy.copy(currentBoard), currentTotalBoard)
        else:
            return (-1) * favorability(copy.copy(currentBoard), currentTotalBoard)
    if (player == 'X'):
        them = 'O'
    else:
        them = 'X'
    moves = []
    if (position == -1):
        for x in range(0, 9):
            if (currentBoard[x] == "."):
                for y in board.possibleMoves(currentTotalBoard, x):
                    moves.append((y, x))
    else:
        for y in board.possibleMoves(currentTotalBoard, position):
            moves.append((y, position))
    if (len(moves) == 0):
        return max_step(copy.copy(currentBoard), copy.copy(currentTotalBoard), -1, depth - 1, alpha, beta, player)
    for nextIndex in moves:
        toMove = board.move(copy.copy(currentBoard), copy.copy(currentTotalBoard), nextIndex[1], them, nextIndex[0])
        z = max_step(toMove[0], toMove[1], toMove[2], depth - 1, alpha, beta, player)
        results.append(z)
        if (z < beta):
            beta = z
        if (beta <= alpha):  # pruning
            break
    if (len(results) != 0):
        return min(results)

def maxMove(currentBoard, currentTotalBoard, position, depth):  # STOP USING GLOBAL VARIABLES
    player = us
    alpha = -10000
    beta = 10000
    results = {}
    moves = []
    if (position == -1):
        for x in range(0, 9):
            if (currentBoard[x] == "."):
                for y in possibleMoves(currentTotalBoard, x):
                    moves.append((y, x))
    else:
        for y in possibleMoves(currentTotalBoard, position):
            moves.append((y, position))
    for nextIndex in moves:
        toMove = move(copy.copy(currentBoard), copy.copy(currentTotalBoard), nextIndex[1], us, nextIndex[0])
        nextBoard = toMove[0]
        nextTotalBoard = toMove[1]
        nextSpot = toMove[2]
        z = min_step(copy.copy(nextBoard), copy.copy(nextTotalBoard), nextSpot, depth - 1, alpha, beta, player)
        toMove = tuple(toMove)
        results[z] = toMove
        if (z > alpha):
            alpha = z
        if (alpha >= beta):  # pruning
            break
    toReturn = 0
    maximum = max(results.keys())
    for x in results.keys():
        if (x == maximum):
            toReturn = x
    return results[toReturn]