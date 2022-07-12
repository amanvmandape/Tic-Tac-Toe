# Tic-Tac-Toe Game

# Variables

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
currentToken = 'X'
winningToken = ''
slotsFilled = 0

print("Tic-Tac-Toe Game")
print("\n Match 3 lines vertically, horizontally or diagonally")
print("\n X goes first then O")

while winningToken == '' and slotsFilled < 9:
    print("\n")
    print("%s|%s|%s" % (board[0], board[1], board[2]))
    print("-+-+-")
    print("%s|%s|%s" % (board[3], board[4], board[5]))
    print("-+-+-")
    print("%s|%s|%s" % (board[6], board[7], board[8]))

    pos = -1
    while pos == -1:
        pos = int(input("\n%s's turn. Where do you want to place?" % currentToken))
        if pos < 1 or pos > 9:
            pos = -1
            print('Invalid Choice, Only 1-9 allowed')

        pos -= 1

        if board[pos] == 'X' or board[pos] == 'O':
            pos = -1
            print(" Place already occupied by %s" % board[pos])

    board[pos] = currentToken
    slotsFilled += 1

    # Rows
    row1 = board[0] == currentToken and board[1] == currentToken and board[2] == currentToken
    row2 = board[3] == currentToken and board[4] == currentToken and board[5] == currentToken
    row3 = board[6] == currentToken and board[7] == currentToken and board[8] == currentToken

    # Cols
    col1 = board[0] == currentToken and board[3] == currentToken and board[6] == currentToken
    col2 = board[1] == currentToken and board[4] == currentToken and board[7] == currentToken
    col3 = board[2] == currentToken and board[5] == currentToken and board[8] == currentToken

    # Diags
    diag1 = board[0] == currentToken and board[4] == currentToken and board[8] == currentToken
    diag2 = board[2] == currentToken and board[4] == currentToken and board[6] == currentToken

    row = row1 or row2 or row3
    col = col1 or col2 or col3
    diag = diag1 or diag2

    if row or col or diag:
        winningToken = currentToken
        print("\n")
        print("%s|%s|%s" % (board[0], board[1], board[2]))
        print("-+-+-")
        print("%s|%s|%s" % (board[3], board[4], board[5]))
        print("-+-+-")
        print("%s|%s|%s" % (board[6], board[7], board[8]))

        print("Congrats, %s has won" % winningToken)

    if currentToken == "X":
        currentToken = "O"
    else:
        currentToken = "X"

if slotsFilled == 9 and winningToken == '':
    print("It's a Draw")
