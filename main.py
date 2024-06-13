import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]

rows = 6
cols = 7


def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
                print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")


def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn


def checkForWinner(chip):
    # Check horizontal spaces
    for x in range(rows):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x][y+1] == chip and gameBoard[x][y+2] == chip and gameBoard[x][y+3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check vertical spaces
    for x in range(rows - 3):
        for y in range(cols):
            if gameBoard[x][y] == chip and gameBoard[x+1][y] == chip and gameBoard[x+2][y] == chip and gameBoard[x+3][y] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper right to bottom left diagonal spaces
    for x in range(rows - 3):
        for y in range(3, cols):
            if gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper left to bottom right diagonal spaces
    for x in range(rows - 3):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True
    return False


def coordinateParser(inputString):
    coordinate = [None] * 2
    if inputString[0] in possibleLetters:
        coordinate[1] = possibleLetters.index(inputString[0])
    else:
        print("Invalid column")
        return None
    try:
        coordinate[0] = int(inputString[1])
        if coordinate[0] < 0 or coordinate[0] >= rows:
            print("Invalid row")
            return None
    except ValueError:
        print("Invalid row input")
        return None
    return coordinate


def isSpaceAvailable(intendedCoordinate):
    return gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == ''


def gravityChecker(intendedCoordinate):
    for row in reversed(range(rows)):
        if isSpaceAvailable([row, intendedCoordinate[1]]):
            return [row, intendedCoordinate[1]]
    return None


leaveLoop = False
turnCounter = 0
while not leaveLoop:
    if turnCounter % 2 == 0:
        printGameBoard()
        while True:
            spacePicked = input("\nChoose a space (e.g., A0): ")
            coordinate = coordinateParser(spacePicked)
            if coordinate:
                coordinate = gravityChecker(coordinate)
                if coordinate:
                    modifyArray(coordinate, '🔵')
                    break
                else:
                    print("Column is full. Choose another column.")
            else:
                print("Invalid input. Try again.")
        winner = checkForWinner('🔵')
        turnCounter += 1
    else:
        while True:
            cpuColumn = random.choice(possibleLetters)
            cpuCoordinate = gravityChecker(
                [0, possibleLetters.index(cpuColumn)])
            if cpuCoordinate:
                modifyArray(cpuCoordinate, '🔴')
                break
        turnCounter += 1
        winner = checkForWinner('🔴')

    if winner or turnCounter == rows * cols:
        printGameBoard()
        if not winner:
            print("\nGame over. It's a tie! Thank you for playing :)")
        break
