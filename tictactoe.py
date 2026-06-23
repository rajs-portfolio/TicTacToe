board = [" "] * 9

def print_board():
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i+1] + "|" + board[i+2])

player = "X"

while " " in board:
    print_board()
    pos = int(input(f"Player {player}, enter position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = player
        player = "O" if player == "X" else "X"
    else:
        print("Position already taken!")

print_board()
print("Game Over!")
