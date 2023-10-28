# issues: Change Global overallBoard, don't place in done overallBoard, favorability
import copy
import board as gameState
import nextMove as computerThink

nextMoves = {}
overallBoard = "........."
allBoards = [".........", ".........", ".........", ".........", ".........", ".........", ".........", ".........", "........."]
computer_1 = ""
computer_2 = ""
NO_BOARD_VALUE = -1
IS_FINISHED_RESULT_X = 1
IS_FINISHED_RESULT_O = -1
IS_FINISHED_RESULT_DRAW = 0
IS_FINISHED_RESULT_INDEX = 1
IS_FINISHED_OVER_YET_INDEX = 0
MOVE_PLAYED_OVERALL_BOARD_INDEX = 0
MOVE_PLAYED_ALL_BOARDS_INDEX = 1
MOVE_PLAYED_BOARD_TO_PLAY_INDEX = 2
COMPUTER_1_DEPTH = 3
COMPUTER_2_DEPTH = 3
COMPUTER_1_METHOD = 2
COMPUTER_2_METHOD = 1

first = input("Which computer goes first (1/2): ")
if first == "1":
    computer_1 = "X"
    computer_2 = "O"
else:
    computer_1 = "O"
    computer_2 = "X"

goesNext = "X"
boardToPlay = NO_BOARD_VALUE
while not gameState.isFinished(overallBoard)[IS_FINISHED_OVER_YET_INDEX]:
    gameState.printBoard(overallBoard, allBoards)
    print(computerThink.favorability(overallBoard, allBoards, 2))
    print("")
    if goesNext == computer_1:
        movePlayed = computerThink.maxMove(copy.copy(overallBoard), copy.copy(allBoards), boardToPlay, COMPUTER_1_DEPTH, computer_1, COMPUTER_1_METHOD)
        overallBoard = movePlayed[MOVE_PLAYED_OVERALL_BOARD_INDEX]
        allBoards = movePlayed[MOVE_PLAYED_ALL_BOARDS_INDEX]
        boardToPlay = movePlayed[MOVE_PLAYED_BOARD_TO_PLAY_INDEX]
        goesNext = computer_2
    else:
        movePlayed = computerThink.maxMove(copy.copy(overallBoard), copy.copy(allBoards), boardToPlay, COMPUTER_2_DEPTH, computer_2, COMPUTER_2_METHOD)
        overallBoard = movePlayed[MOVE_PLAYED_OVERALL_BOARD_INDEX]
        allBoards = movePlayed[MOVE_PLAYED_ALL_BOARDS_INDEX]
        boardToPlay = movePlayed[MOVE_PLAYED_BOARD_TO_PLAY_INDEX]
        goesNext = computer_1
    print("_________________")
    print("")
gameState.printBoard(overallBoard, allBoards)
finalResults = gameState.isFinished(overallBoard)
if finalResults[IS_FINISHED_RESULT_INDEX] == IS_FINISHED_RESULT_DRAW:
    print("draw")
if finalResults[IS_FINISHED_RESULT_INDEX] == IS_FINISHED_RESULT_X:
    print("X wins")
if finalResults[IS_FINISHED_RESULT_INDEX] == IS_FINISHED_RESULT_O:
    print("O wins")
