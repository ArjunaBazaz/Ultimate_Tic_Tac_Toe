# issues: Change Global overallBoard, don't place in done overallBoard, favorability
import copy
import board as gameState
import nextMove as computerThink

nextMoves = {}
#mainBoard = "........."
#allBoards = [".........", ".........", ".........", ".........", ".........", ".........", ".........", ".........", "........."]
computer_1 = "X"
computer_2 = "O"
NO_BOARD_VALUE = -1
IS_FINISHED_RESULT_X = 1
IS_FINISHED_RESULT_O = -1
IS_FINISHED_RESULT_DRAW = 0
IS_FINISHED_RESULT_INDEX = 1
IS_FINISHED_OVER_YET_INDEX = 0
MOVE_PLAYED_OVERALL_BOARD_INDEX = 0
MOVE_PLAYED_ALL_BOARDS_INDEX = 1
MOVE_PLAYED_BOARD_TO_PLAY_INDEX = 2
COMPUTER_1_DEPTH = 4
COMPUTER_2_DEPTH = 4
COMPUTER_1_METHOD = 2
COMPUTER_2_METHOD = 1
NUM_TESTS = 5

def play(totalBoard, currentTotalBoard, computer_1, computer_2):
    goesNext = "X"
    boardToPlay = NO_BOARD_VALUE
    while not gameState.isFinished(totalBoard)[IS_FINISHED_OVER_YET_INDEX]:
        if goesNext == computer_1:
            movePlayed = computerThink.maxMove(copy.copy(totalBoard), copy.copy(currentTotalBoard), boardToPlay, COMPUTER_1_DEPTH, computer_1, COMPUTER_1_METHOD)
            totalBoard = movePlayed[MOVE_PLAYED_OVERALL_BOARD_INDEX]
            currentTotalBoard = movePlayed[MOVE_PLAYED_ALL_BOARDS_INDEX]
            boardToPlay = movePlayed[MOVE_PLAYED_BOARD_TO_PLAY_INDEX]
            goesNext = computer_2
        else:
            movePlayed = computerThink.maxMove(copy.copy(totalBoard), copy.copy(currentTotalBoard), boardToPlay, COMPUTER_2_DEPTH, computer_2, COMPUTER_2_METHOD)
            totalBoard = movePlayed[MOVE_PLAYED_OVERALL_BOARD_INDEX]
            currentTotalBoard = movePlayed[MOVE_PLAYED_ALL_BOARDS_INDEX]
            boardToPlay = movePlayed[MOVE_PLAYED_BOARD_TO_PLAY_INDEX]
            goesNext = computer_1
    return (totalBoard, currentTotalBoard)

total1Wins = 0
total2Wins = 0
totalDraws = 0
for i in range(0, NUM_TESTS):
    gameResult = play(".........", [".........", ".........", ".........", ".........", ".........", ".........", ".........", ".........", "........."], "X", "O")
    gameState.printBoard(gameResult[0], gameResult[1])
    finalResults = gameState.isFinished(gameResult[0])
    if finalResults[IS_FINISHED_RESULT_INDEX] == IS_FINISHED_RESULT_DRAW:
        totalDraws = totalDraws + 1
    if finalResults[IS_FINISHED_RESULT_INDEX] == IS_FINISHED_RESULT_X:
        total1Wins = total1Wins + 1
    if finalResults[IS_FINISHED_RESULT_INDEX] == IS_FINISHED_RESULT_O:
        total2Wins = total2Wins + 1
for i in range(0, NUM_TESTS):
    gameResult = play(".........", [".........", ".........", ".........", ".........", ".........", ".........", ".........", ".........", "........."], "O", "X")
    gameState.printBoard(gameResult[0], gameResult[1])
    finalResults = gameState.isFinished(gameResult[0])
    if finalResults[IS_FINISHED_RESULT_INDEX] == IS_FINISHED_RESULT_DRAW:
        totalDraws = totalDraws + 1
    if finalResults[IS_FINISHED_RESULT_INDEX] == IS_FINISHED_RESULT_X:
        total2Wins = total2Wins + 1
    if finalResults[IS_FINISHED_RESULT_INDEX] == IS_FINISHED_RESULT_O:
        total1Wins = total1Wins + 1

print("Computer 1 Wins:", total1Wins)
print("Computer 2 Wins:", total2Wins)
print("Draws:", totalDraws)
