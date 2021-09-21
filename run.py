from random import randint

board = []
"""
FIRST THE 2 BOARDS CREAT THE BOARDS
"""
MY_BOARD = [[" "] * 8 for x in range(8)]
HIS_BOARD = [[" "] * 8 for x in range(8)]

"""
converting the numbers to letter
"""
numbers = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

"""
printing the boards
"""


def create_board(board):
    print('  a b c d e f g h')
    print("  ---------------")
    rows = 1
    for row in board:
        print("%d|%s|" % (rows, "/". join(row)))
        rows += 1

"""
Creating the ships to sink for the game
"""


def ships(board):
    for ship in range(5):
        ship_verticle, ship_horizontal = randint(0, 7), randint(0, 7)
        while board[ship_verticle][ship_horizontal] == "X":
            ship_verticle, ship_horizontal = randint(0, 7), randint(0, 7)
        board[ship_verticle][ship_horizontal] = "X"

"""
To define hiting the location of the ships in the game
"""


def location_ship():
    row = input("Enter number between: 1-8 \n")
    while row not in "12345678":
        print("Wrong input number out side of 1-8")
        row = input("Enter number between 1-8")
    column = input("Enter a letter between a-h \n").lower()
    while column not in "abcdefgh":
        print("Wrong input letter should be between a-h")
        column = input("Enter a letter between a-h \n").lower()
    return int(row) - 1, numbers[column]

"""
what happens when you hit a ship
"""


def ship_hit(board):
    hit = 0
    for row in board:
        for column in row:
            if column == "X":
                hit += 1
    return hit

ships(MY_BOARD)
turns = 12
while turns > 0:
    print("TIME for Battle Ship\n")
    print("Pick your shot")
    create_board(HIS_BOARD)
    row, column = location_ship()
    if HIS_BOARD[row][column] == "-":
        print("Thats the same entry try again")
    elif MY_BOARD[row][column] == "X":
        print("HIT!!! you hit my ship :( ")
        HIS_BOARD[row][column] = "X"
        turns -= 1
    else:
        print("HAHAHA you missed my ship :) ")
        HIS_BOARD[row][column] = "-"
        turns -= 1
    if ship_hit(HIS_BOARD) == 5:
        print("YOU SANK MY BATTLE SHIPS WINNER\n")
        break
    print("Turns Left:  " + str(turns))
    print("-----------------------------------------------")
    if turns == 0:
        print("game over restart")
        break
# X means you hit the ship
# - means a miss
