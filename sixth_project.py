# Tic Tac Game
def tic_tac(board):

    print(f"{board[0]} {board[1]} {board[2]}")
    print(f"{board[3]} {board[4]} {board[5]}")
    print(f"{board[6]} {board[7]} {board[8]}")


current_player = 1

Board = [
        '*','*','*',
        '*','*','*',
        '*','*','*'
        ]
def checker(board):
    if (board[0]==board[1]==board[2] == 'X' or
        board[3]==board[4]==board[5] == 'X' or
        board[6]==board[7]==board[8] == 'X' or
        board[6]==board[7]==board[8] == 'X' or
        board[0]==board[6]==board[3] == 'X' or
        board[1]==board[4]==board[7] == 'X' or
        board[2]==board[5]==board[8] == 'X' or
        board[0]==board[4]==board[8] == 'X' or
        board[2]==board[4]==board[6] =='X'):
        print(f"player: {current_player} win match !!!!")
        exit()
    elif (board[0]==board[1]==board[2] == 'O' or
        board[3]==board[4]==board[5] == 'O' or
        board[6]==board[7]==board[8] == 'O' or
        board[0]==board[6]==board[3] == 'O' or
        board[1]==board[4]==board[7] == 'O' or
        board[2]==board[5]==board[8] == 'O' or
        board[0]==board[4]==board[8] == 'O' or
        board[2]==board[4]==board[6] == 'O'):
        print(f"{current_player} win match !!!!")
        exit()
    elif '*' not in board:
        print("Nice its a tie !!")
        exit()
    return False

tic_tac(Board)
while True:
    n = int(input(f"Enter player{current_player} \n"))
    if current_player == 1:
        if Board[n-1] =='O' or Board[n-1] == 'X':
            print(" O or X is already grant")
            continue
        Board[n - 1] = 'X'
        checker(Board)
        current_player = 0
    elif current_player == 0:
        if Board[n-1] =='O' or Board[n-1] == 'X':
            print(" O or X is already grant")
            continue
        Board[n - 1] = 'O'
        checker(Board)
        current_player = 1

    tic_tac(Board)

