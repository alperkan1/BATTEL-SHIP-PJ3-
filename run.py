from random import randint

board = []
"""
FIRST THE 2 BOARDS CREAT THE BOARDS
"""
MY_BOARD = [[" "] * 8 for x in range (8)]
HIS_BOARD = [[" "] * 8 for x in range (8)]

"""
converting the numbers to letter
"""
numbers = {"a":0, "b":1, "c":3, "d":4, "e":5, "f":5, "g":6, "h":7}

"""
printing the boards
"""
def create_board(board):
    print('a b c d e f g h')
    print("---------------")
    rows = 1
    for row in board:
        print("%d|%s|" % (rows, "/". join(row)))
        rows += 1
"""
Creating the ships to sink for the game 
"""        
def ships(board):
    for ship in range(5):
        ship_verticle, ship_horizontal = randint(0,7), randint(0,7)
        while board[ship_verticle][ship_horizontal] == "X":
            ship_verticle, ship_horizontal = randint(0,7), randint(0,7)
        board[ship_verticle][ship_horizontal] = "X"

"""
To define hiting the location of the ships in the game 
"""

def location_ship():
    row = input("Enter number between 1-8")
    while row not in "12345678" or ValueError:
        print("Wrong input number out side of 1-8")
        row = input("Enter number between 1-8")
    column = input("Enter a letter between a-h").lower()
    while column not in "abcdefgh" or ValueError:
        print("Wrong input letter should be between a-h").lower()
        input("Enter a letter between a-h").lower()
    return int(row) - 1, numbers[column]

"""
what happens when you hit a ship
"""

def ship_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

ships(HIS_BOARD)
turns = 12
create_board(HIS_BOARD)