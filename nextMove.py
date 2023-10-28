import random
import copy
import board as gameState

NO_BOARD_VALUE = -1
IS_FINISHED_RESULT_INDEX = 1
IS_FINISHED_OVER_YET_INDEX = 0
MOVE_PLAYED_OVERALL_BOARD_INDEX = 0
MOVE_PLAYED_ALL_BOARDS_INDEX = 1
MOVE_PLAYED_BOARD_TO_PLAY_INDEX = 2
A = 20
B = 1
C = 5
D = 1
E1 = 1000
F1 = 1
G1 = 25
H1 = 1
E2 = 1000
F2 = 1
G2 = 35
H2 = 1

def scoreBoard(currentBoard):
    XScore = 0
    OScore = 0
    finished = gameState.isFinished(currentBoard)
    if finished[IS_FINISHED_OVER_YET_INDEX]:
        return A * finished[IS_FINISHED_RESULT_INDEX]
    for x in range(0, 9):
        if currentBoard[x] == 'X':
            XScore = XScore + B
        elif currentBoard[x] == 'O':
            OScore = OScore + B
        else:
            tempBoard = currentBoard[0:x] + "X" + currentBoard[x + 1:]
            if gameState.isFinished(tempBoard)[IS_FINISHED_OVER_YET_INDEX]:
                XScore = XScore + C
            tempBoard = currentBoard[0:x] + "O" + currentBoard[x + 1:]
            if gameState.isFinished(tempBoard)[IS_FINISHED_OVER_YET_INDEX]:
                OScore = OScore + C
        if x == 4:
            if currentBoard[x] == 'X':
                XScore = XScore + D
            elif currentBoard[x] == 'O':
                OScore = OScore + D
    return XScore - OScore

def favorability2(currentBoard, currentTotalBoard):     #fix the line when it checks if adding an X or O would make a change to the game state
    totalScore = 0
    finished = gameState.isFinished(currentBoard)
    if finished[IS_FINISHED_OVER_YET_INDEX]:
        return E1 * scoreBoard(currentBoard)
    for x in range(0, 9):
        totalScore = totalScore + F1 * scoreBoard(currentTotalBoard[x])
        if(gameState.isFinished(currentTotalBoard[x])[IS_FINISHED_OVER_YET_INDEX]):
            continue
        elif gameState.isFinished(currentBoard[0:x] + "X" + currentBoard[x + 1:])[IS_FINISHED_OVER_YET_INDEX]:
            totalScore = totalScore + G1 * (2 ** (scoreBoard(currentTotalBoard[x]) / 20))
        elif gameState.isFinished(currentBoard[0:x] + "O" + currentBoard[x + 1:])[IS_FINISHED_OVER_YET_INDEX]:
            totalScore = totalScore - G1 * (2 ** (scoreBoard(currentTotalBoard[x]) / 20))
        if x == 4:
            totalScore = totalScore + H1 * scoreBoard(currentTotalBoard[x])
    return totalScore

def favorability1(currentBoard, currentTotalBoard):  # FINISH FAVORABILITY
    totalScore = 0
    finished = gameState.isFinished(currentBoard)
    if finished[IS_FINISHED_OVER_YET_INDEX]:
        return E2 * scoreBoard(currentBoard)
    for x in range(0, 9):
        totalScore = totalScore + F2 * scoreBoard(currentTotalBoard[x])
        if(gameState.isFinished(currentTotalBoard[x])[IS_FINISHED_OVER_YET_INDEX]):
            continue
        elif gameState.isFinished(currentBoard[0:x] + "X" + currentBoard[x + 1:])[IS_FINISHED_OVER_YET_INDEX]:
            totalScore = totalScore + G2 * (2 ** (scoreBoard(currentTotalBoard[x]) / 20))
        elif gameState.isFinished(currentBoard[0:x] + "O" + currentBoard[x + 1:])[IS_FINISHED_OVER_YET_INDEX]:
            totalScore = totalScore - G2 * (2 ** (scoreBoard(currentTotalBoard[x]) / 20))
        if x == 4:
            totalScore = totalScore + H2 * scoreBoard(currentTotalBoard[x])
    return totalScore

def favorability(currentBoard, currentTotalBoard, method):
    if method == 1:
        return favorability1(currentBoard, currentTotalBoard)*(random.random()/100 + 0.995)
    else:
        return favorability2(currentBoard, currentTotalBoard)*(random.random()/100 + 0.995)


def max_step(currentBoard, currentTotalBoard, position, depth, alpha, beta, player, method):  # Whatif no moves available
    finished = gameState.isFinished(currentBoard)
    results = []
    if depth == 0 or finished[IS_FINISHED_OVER_YET_INDEX]:
        if player == "X":
            return favorability(copy.copy(currentBoard), currentTotalBoard, method)
        else:
            return (-1) * favorability(copy.copy(currentBoard), currentTotalBoard, method)
    moves = []
    if position == NO_BOARD_VALUE:
        for x in range(0, 9):
            if currentBoard[x] == ".":
                for y in gameState.possibleMoves(currentTotalBoard, x):
                    moves.append((y, x))
    else:
        for y in gameState.possibleMoves(currentTotalBoard, position):
            moves.append((y, position))
    if len(moves) == 0:
        return min_step(copy.copy(currentBoard), copy.copy(currentTotalBoard), -1, depth - 1, alpha, beta, player)
    for nextIndex in moves:
        toMove = gameState.move(copy.copy(currentBoard), copy.copy(currentTotalBoard), nextIndex[1], player, nextIndex[0])
        min = min_step(toMove[MOVE_PLAYED_OVERALL_BOARD_INDEX], toMove[MOVE_PLAYED_ALL_BOARDS_INDEX], toMove[MOVE_PLAYED_BOARD_TO_PLAY_INDEX], depth - 1, alpha, beta, player, method)
        results.append(min)
        if min > alpha:
            alpha = min
        if beta <= alpha:  # pruning
            break
    if len(results) != 0:
        return max(results)


def min_step(currentBoard, currentTotalBoard, position, depth, alpha, beta, player, method):
    finished = gameState.isFinished(currentBoard)
    results = []
    if depth == 0 or finished[IS_FINISHED_OVER_YET_INDEX]:
        if player == "X":
            return favorability(copy.copy(currentBoard), currentTotalBoard, method)
        else:
            return (-1) * favorability(copy.copy(currentBoard), currentTotalBoard, method)
    if player == 'X':
        them = 'O'
    else:
        them = 'X'
    moves = []
    if position == NO_BOARD_VALUE:
        for x in range(0, 9):
            if currentBoard[x] == ".":
                for y in gameState.possibleMoves(currentTotalBoard, x):
                    moves.append((y, x))
    else:
        for y in gameState.possibleMoves(currentTotalBoard, position):
            moves.append((y, position))
    if len(moves) == 0:
        return max_step(copy.copy(currentBoard), copy.copy(currentTotalBoard), -1, depth - 1, alpha, beta, player)
    for nextIndex in moves:
        toMove = gameState.move(copy.copy(currentBoard), copy.copy(currentTotalBoard), nextIndex[1], them, nextIndex[0])
        max = max_step(toMove[MOVE_PLAYED_OVERALL_BOARD_INDEX], toMove[MOVE_PLAYED_ALL_BOARDS_INDEX], toMove[MOVE_PLAYED_BOARD_TO_PLAY_INDEX], depth - 1, alpha, beta, player, method)
        results.append(max)
        if max < beta:
            beta = max
        if beta <= alpha:  # pruning
            break
    if len(results) != 0:
        return min(results)

def maxMove(currentBoard, currentTotalBoard, position, depth, playerXorO, method):
    player = playerXorO
    alpha = -100000
    beta = 100000
    results = {}
    moves = []
    if position == NO_BOARD_VALUE:
        for x in range(0, 9):
            if currentBoard[x] == ".":
                for y in gameState.possibleMoves(currentTotalBoard, x):
                    moves.append((y, x))
    else:
        for y in gameState.possibleMoves(currentTotalBoard, position):
            moves.append((y, position))
    for nextIndex in moves:
        toMove = gameState.move(copy.copy(currentBoard), copy.copy(currentTotalBoard), nextIndex[1], playerXorO, nextIndex[0])
        nextBoard = toMove[MOVE_PLAYED_OVERALL_BOARD_INDEX]
        nextTotalBoard = toMove[MOVE_PLAYED_ALL_BOARDS_INDEX]
        nextSpot = toMove[MOVE_PLAYED_BOARD_TO_PLAY_INDEX]
        min = min_step(copy.copy(nextBoard), copy.copy(nextTotalBoard), nextSpot, depth - 1, alpha, beta, player, method)
        toMove = tuple(toMove)
        results[min] = toMove
        if min > alpha:
            alpha = min
        if alpha >= beta:  # pruning
            break
    toReturn = 0
    maximum = max(results.keys())
    for x in results.keys():
        if x == maximum:
            toReturn = x
            break
    return results[toReturn]
