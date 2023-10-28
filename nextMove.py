import random
import copy
import board as gameState

NO_BOARD_VALUE = -1
IS_FINISHED_RESULT_INDEX = 1
IS_FINISHED_OVER_YET_INDEX = 0
MOVE_PLAYED_OVERALL_BOARD_INDEX = 0
MOVE_PLAYED_ALL_BOARDS_INDEX = 1
MOVE_PLAYED_BOARD_TO_PLAY_INDEX = 2

def scoreBoard(currentBoard):
    XScore = 0
    OScore = 0
    finished = gameState.isFinished(currentBoard)
    if finished[IS_FINISHED_OVER_YET_INDEX]:
        return 50 * finished[IS_FINISHED_RESULT_INDEX]
    for x in range(0, 9):
        if currentBoard[x] == 'X':
            XScore = XScore + 4
        elif currentBoard[x] == 'O':
            OScore = OScore + 4
        else:
            tempBoard = currentBoard[0:x] + "X" + currentBoard[x + 1:]
            if gameState.isFinished(tempBoard)[IS_FINISHED_OVER_YET_INDEX]:
                XScore = XScore + 6
            tempBoard = currentBoard[0:x] + "O" + currentBoard[x + 1:]
            if gameState.isFinished(tempBoard)[IS_FINISHED_OVER_YET_INDEX]:
                OScore = OScore + 6
        if x == 4:
            if currentBoard[x] == 'X':
                XScore = XScore + 2
            elif currentBoard[x] == 'O':
                OScore = OScore + 2
    return XScore - OScore

def favorability2(currentBoard, currentTotalBoard):
    totalScore = 0
    finished = gameState.isFinished(currentBoard)
    if finished[IS_FINISHED_OVER_YET_INDEX]:
        return 50 * finished[IS_FINISHED_RESULT_INDEX]
    for x in range(0, 9):
        totalScore = totalScore + scoreBoard(currentTotalBoard[x])
        tempBoard = currentBoard[0:x] + "X" + currentBoard[x + 1:]
        if gameState.isFinished(tempBoard)[IS_FINISHED_OVER_YET_INDEX]:
            totalScore = totalScore + 2*scoreBoard(currentTotalBoard[x])
        tempBoard = currentBoard[0:x] + "O" + currentBoard[x + 1:]
        if gameState.isFinished(tempBoard)[IS_FINISHED_OVER_YET_INDEX]:
            totalScore = totalScore + 2*scoreBoard(currentTotalBoard[x])
        if x == 4:
            totalScore = totalScore + scoreBoard(currentTotalBoard[x])
    return totalScore

def favorability1(currentBoard, currentTotalBoard):  # FINISH FAVORABILITY
    XScore = 0
    OScore = 0
    totalScore = 0
    finished = gameState.isFinished(currentBoard)
    if finished[IS_FINISHED_OVER_YET_INDEX]:
        return 10000 * finished[IS_FINISHED_RESULT_INDEX]
    for x in range(0, 9):
        if currentBoard[x] == 'X':
            XScore = XScore + 40
            if x % 3 < 2 and currentBoard[x + 1] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 1])
            elif x % 3 != 0 and currentBoard[x - 1] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 1])
            elif x < 6 and currentBoard[x + 3] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 3])
            elif x > 2 and currentBoard[x - 3] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 3])
            elif x % 3 < 2 and x < 6 and currentBoard[x + 4] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 4])
            elif x % 3 != 0 and x > 2 and currentBoard[x - 4] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 4])
            elif x % 3 != 0 and x < 6 and currentBoard[x + 2] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 2])
            elif x % 3 < 2 and x > 2 and currentBoard[x - 2] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 2])
        elif currentBoard[x] == 'O':
            OScore = OScore + 40
            if x % 3 < 2 and currentBoard[x + 1] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 1])
            elif x % 3 != 0 and currentBoard[x - 1] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 1])
            elif x < 6 and currentBoard[x + 3] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 3])
            elif x > 2 and currentBoard[x - 3] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 3])
            elif x % 3 < 2 and x < 6 and currentBoard[x + 4] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 4])
            elif x % 3 != 0 and x > 2 and currentBoard[x - 4] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 4])
            elif x % 3 != 0 and x < 6 and currentBoard[x + 2] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x + 2])
            elif x % 3 < 2 and x != 2 and currentBoard[x - 2] == ".":
                totalScore = totalScore + scoreBoard(currentTotalBoard[x - 2])
        else:
            tempBoard = currentBoard[0:x] + "X" + currentBoard[x + 1:]
            if gameState.isFinished(tempBoard)[IS_FINISHED_OVER_YET_INDEX]:
                XScore = XScore + 100
                totalScore = totalScore + 4 * scoreBoard(currentTotalBoard[x])
            tempBoard = currentBoard[0:x] + "O" + currentBoard[x + 1:]
            if gameState.isFinished(tempBoard)[IS_FINISHED_OVER_YET_INDEX]:
                OScore = OScore + 100
                totalScore = totalScore + 4 * scoreBoard(currentTotalBoard[x])
            totalScore = totalScore + scoreBoard(currentTotalBoard[x])
        if x == 0 or x == 2 or x == 6 or x == 8:
            if currentBoard[x] == 'X':
                XScore = XScore + 10
            elif currentBoard[x] == 'O':
                OScore = OScore + 10
            else:
                totalScore = totalScore + scoreBoard(currentTotalBoard[x])
        if x == 4:
            if currentBoard[x] == 'X':
                XScore = XScore + 25
            elif currentBoard[x] == 'O':
                OScore = OScore + 25
            else:
                totalScore = totalScore + 2 * scoreBoard(currentTotalBoard[x])
    return totalScore + XScore - OScore

def favorability(currentBoard, currentTotalBoard, method):
    if method == 1:
        return favorability1(currentBoard, currentTotalBoard)
    else:
        return favorability2(currentBoard, currentTotalBoard)


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
    alpha = -10000
    beta = 10000
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
