# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

SUDOKU_2 = [
    [[0, 0, 0], [0, 6, 0], [0, 5, 0]],  # SQUARE 1
    [[6, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[2, 0, 0], [7, 3, 0], [0, 6, 8]],
    [[0, 8, 0], [0, 7, 5], [4, 3, 0]],  # SQUARE 2
    [[3, 7, 0], [0, 9, 0], [0, 0, 6]],
    [[0, 0, 0], [0, 0, 0], [7, 0, 9]],
    [[0, 0, 0], [3, 4, 0], [0, 0, 5]],  # SQUARE 3
    [[7, 0, 4], [5, 8, 2], [9, 0, 3]],
    [[8, 0, 0], [0, 0, 0], [0, 4, 0]]
]

SUDOKU_SOLVED = [
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
]

MAX_SQUARES = 9


def print_Sudoku():
    squares = 0

    for squares in range(MAX_SQUARES):
        print(SUDOKU_2[squares])
        squares += 1


def check_Square(y, x):
    toReturnNumbers = []
    # Round y to the nearest starting point which are 0, 3 and 6
    maxRange = 0
    if y < 3:
        y = 0
        maxRange = 3
    elif y < 6:
        y = 3
        maxRange = 6
    elif y > 6:
        y = 6
        maxRange = 9

    # Python in range function does not include the last number. It's a < not a <=
    while y < maxRange:
        j = 0
        for j in range(j + 3):
            squareNumber = SUDOKU_2[y][x][j]
            if squareNumber != 0:
                toReturnNumbers.append(squareNumber)
            j += 1
        y += 1

    return toReturnNumbers


def check_Horizontal(y):
    toReturnNumbers = []

    x = 0
    for x in range(x + 3):
        j = 0
        for j in range(j + 3):
            squareNumber = SUDOKU_2[y][x][j]
            if squareNumber != 0:
                toReturnNumbers.append(squareNumber)
            j += 1
        x += 1

    return toReturnNumbers


def check_Vertical(x, j):
    toReturnNumbers = []

    y = 0
    for y in range(9):
        squareNumber = SUDOKU_2[y][x][j]
        if squareNumber != 0:
            toReturnNumbers.append(squareNumber)
        y += 1

    return toReturnNumbers


def check_Correct_Number(avaiableNumbers, squareNumbers, horizontalNumbers, verticalNumbers):
    toReturnNumbers = []
    i = 0
    for i in range(len(avaiableNumbers)):
        if avaiableNumbers[i] not in squareNumbers:
            if avaiableNumbers[i] not in horizontalNumbers:
                if avaiableNumbers[i] not in verticalNumbers:
                    toReturnNumbers.append(avaiableNumbers[i])
        i += 1

    return toReturnNumbers


def loop_Start():
    print("Starting to resolve sudoku")
    # ROWS
    y = 0
    # COLUMNS
    z = 0
    # NUMBERS
    j = 0
    # LIST OF NUMBERS
    LIST_OF_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # CONTROLS IF THE SUDOKU IS COMPLETED
    isCompleted = True
    # CONTROLS IF THE PROGRAM IS IN A INFINITE LOOP
    anyNumberSet = False

    for y in range(9):
        for x in range(3):
            for j in range(3):
                numberInPosition = SUDOKU_2[y][x][j]
                if numberInPosition != 0:
                    continue

                isCompleted = False

                avaiableNumbers = LIST_OF_NUMBERS
                squareNumbers = check_Square(y, x)
                horizontalNumbers = check_Horizontal(y)
                verticalNumbers = check_Vertical(x, j)
                correctNumber = check_Correct_Number(avaiableNumbers, squareNumbers, horizontalNumbers, verticalNumbers)

                if len(correctNumber) <= 1: # Only one avaiable solution
                    SUDOKU_2[y][x][j] = correctNumber[0]
                    anyNumberSet = True

                j += 1
            x += 1
        y += 1

    if isCompleted:
        print("Congrats, the program does not have any bug...")
        print_Sudoku()
    else:
        if not anyNumberSet:
            print("Infinite loop found! Check your algorithm newbie")
            print_Sudoku()
        else:
            loop_Start()


if __name__ == '__main__':
    loop_Start()
    # print_sudoku()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
