ROWS = 6
COLUMNS = 7


def printboard():
    for row in board:
        for col in row:
            print(col + " ", end='')
        print()


def placecoin():  # return True/False to indicate success in placing the coin
    # find the first unfilled row/hole in the specified column
    rowin = len(board) - 1
    while board[rowin][colin] != "-":
        rowin -= 1
        if rowin < 0:
            return False

    if rowin >= 0:
        board[rowin][colin] = pnum
        return True


def fourinarow():  # checks for 4-in-a-rows on the board
    # loop from bottom to top, left to right
    for r in range(len(board)-1, -1, -1):  # 5, 4, 3, 2, 1, 0
        for c in range(COLUMNS):
            if c <= 3:  # coin is in left half of board
                if checkforline(r, c, 0, 1) or checkforline(r, c, -1, 1):  # checks for horiz & bltr line
                    return True
            if c >= 3:  # coin is in right half of board
                if checkforline(r, c, -1, -1):  # checks for brtl line
                    return True
            if r >= 3:  # coin is in bottom half of board
                if checkforline(r, c, -1, 0):  # checks for vert line
                    return True
    return False


def checkforline(r, c, rinc, cinc):  # row increment & column increment
    if board[r][c] != "-":
        if board[r][c] == board[r+rinc][c+cinc] == board[r+2*rinc][c+2*cinc] == board[r+3*rinc][c+3*cinc]:
            return True
    return False


board = [["-" for i in range(COLUMNS)] for j in range(ROWS)]  # create 7x6 connect-4 board
printboard()

turnnum = 0
while fourinarow() is False:
    pnum = str(turnnum % 2 + 1)  # player number
    if turnnum > 41:  # if the board is full (i.e. there have already been 42 turns)
        print("It's a draw!")
        break

    colinstr = input("Player " + pnum + ", type the column (1-7) you want to place your coin in: ")
    if colinstr in (str(n) for n in range(1, 8)):  # proceed if the input is a number from 1-7
        colin = int(colinstr) - 1  # the actual integer for the column input
        if placecoin() is True:  # place the coin; procceed if successful (if the column isn't full)
            printboard()
            if turnnum >= 6 and fourinarow() is True:  # only check for 4-in-a-row if there have been at least 7 turns
                print("Player " + pnum + " wins!")
            turnnum += 1
        else:
            print("That column is full.")
    else:
        print("Make sure it's one number from 1 to 7.")
