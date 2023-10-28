# issues: Change Global overallBoard, don't place in done overallBoard, favorability
import copy
import board as gameState
import nextMove as computerThink

nextMoves = {}
overallBoard = "........."
allBoards = [".........", ".........", ".........", ".........", ".........", ".........", ".........", ".........", "........."]
player = ""
computer = ""
NO_BOARD_VALUE = -1
IS_FINISHED_RESULT_X = 1
IS_FINISHED_RESULT_O = -1
IS_FINISHED_RESULT_DRAW = 0
IS_FINISHED_RESULT_INDEX = 1
IS_FINISHED_OVER_YET_INDEX = 0
MOVE_PLAYED_OVERALL_BOARD_INDEX = 0
MOVE_PLAYED_ALL_BOARDS_INDEX = 1
MOVE_PLAYED_BOARD_TO_PLAY_INDEX = 2
COMPUTER_DEPTH = 4
COMPUTER_METHOD = 2

first = input("Who goes first (computer/player): ")
if first == "computer":
    player = "X"
    computer = "O"
else:
    player = "O"
    computer = "X"

goesNext = "X"
boardToPlay = NO_BOARD_VALUE
while not gameState.isFinished(overallBoard)[IS_FINISHED_OVER_YET_INDEX]:
    print(computerThink.favorability(overallBoard, allBoards, COMPUTER_METHOD))
    gameState.printBoard(overallBoard, allBoards)
    print("")
    if goesNext == player:
        print("computer's turn")
        movePlayed = computerThink.maxMove(copy.copy(overallBoard), copy.copy(allBoards), boardToPlay, COMPUTER_DEPTH, player, COMPUTER_METHOD)
        overallBoard = movePlayed[MOVE_PLAYED_OVERALL_BOARD_INDEX]
        allBoards = movePlayed[MOVE_PLAYED_ALL_BOARDS_INDEX]
        boardToPlay = movePlayed[MOVE_PLAYED_BOARD_TO_PLAY_INDEX]
        goesNext = computer
        print("")
    else:
        if boardToPlay == NO_BOARD_VALUE:
            boardToPlay = int(input("Which overallBoard would you like you like to play: "))
        if overallBoard[boardToPlay] != ".":
            print("board already won")
            print("")
            continue
        print("your turn in overallBoard:", boardToPlay)
        positionPlayed = int(input("Where do you play (0-8): "))
        if allBoards[boardToPlay][positionPlayed] != ".":
            print("cant play there")
            print("")
            continue
        movePlayed = gameState.move(overallBoard, allBoards, boardToPlay, computer, positionPlayed)
        overallBoard = movePlayed[MOVE_PLAYED_OVERALL_BOARD_INDEX]
        allBoards = movePlayed[MOVE_PLAYED_ALL_BOARDS_INDEX]
        boardToPlay = movePlayed[MOVE_PLAYED_BOARD_TO_PLAY_INDEX]
        goesNext = player
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
