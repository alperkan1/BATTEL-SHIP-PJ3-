from random import randint

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
        print("%d|%s|" % (rows, "/" . join(row)))
        rows += 1
"""
Creating the ships to sink for the game 
"""        
def ships():
    for ship in range(5):
        ship_verticle, ship_horizontal = randint(0,7), randint(0,7)
        while board[ship_verticle][ship_horizontal] == "X":
            ship_verticle, ship_horizontal = randint(0,7), randint(0,7)
        board[ship_verticle][ship_horizontal] = "X"
