import board as gameState

nextMoves = {}
overallBoard = "........."
allBoards = [".........", ".........", ".........", ".........", ".........", ".........", ".........", ".........", "........."]
player_1 = ""
player_2 = ""
NO_BOARD_VALUE = -1
IS_FINISHED_RESULT_X = 1
IS_FINISHED_RESULT_O = -1
IS_FINISHED_RESULT_DRAW = 0
IS_FINISHED_RESULT_INDEX = 1
IS_FINISHED_OVER_YET_INDEX = 0
MOVE_PLAYED_OVERALL_BOARD_INDEX = 0
MOVE_PLAYED_ALL_BOARDS_INDEX = 1
MOVE_PLAYED_BOARD_TO_PLAY_INDEX = 2

first = input("Which Player goes first (1/2): ")
if first == "1":
    player_1 = "X"
    player_2 = "O"
else:
    player_1 = "O"
    player_2 = "X"

goesNext = "X"
boardToPlay = NO_BOARD_VALUE
while not gameState.isFinished(overallBoard)[IS_FINISHED_OVER_YET_INDEX]:
    gameState.printBoard(overallBoard, allBoards)
    print("")
    if goesNext == player_2:
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
        movePlayed = gameState.move(overallBoard, allBoards, boardToPlay, player_2, positionPlayed)
        overallBoard = movePlayed[MOVE_PLAYED_OVERALL_BOARD_INDEX]
        allBoards = movePlayed[MOVE_PLAYED_ALL_BOARDS_INDEX]
        boardToPlay = movePlayed[MOVE_PLAYED_BOARD_TO_PLAY_INDEX]
        goesNext = player_1
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
        movePlayed = gameState.move(overallBoard, allBoards, boardToPlay, player_1, positionPlayed)
        overallBoard = movePlayed[MOVE_PLAYED_OVERALL_BOARD_INDEX]
        allBoards = movePlayed[MOVE_PLAYED_ALL_BOARDS_INDEX]
        boardToPlay = movePlayed[MOVE_PLAYED_BOARD_TO_PLAY_INDEX]
        goesNext = player_2
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