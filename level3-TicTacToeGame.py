from os import system, name

def clear():
    system('cls' if name == 'nt' else 'clear')

def print_board(board):
    print(f"""
|###########|
| {board[1]} # {board[2]} # {board[3]} |
|###########|
| {board[4]} # {board[5]} # {board[6]} |
|###########|
| {board[7]} # {board[8]} # {board[9]} |
|###########|
""")

def check_win(player_moves):
    winning_combinations = [
        [1,2,3], [4,5,6], [7,8,9],
        [1,4,7], [2,5,8], [3,6,9],
        [1,5,9], [3,5,7]
    ]
    for combo in winning_combinations:
        if all(pos in player_moves for pos in combo):
            return True
    return False


# Initialize board
board = {i: str(i) for i in range(1, 10)}

player_X = []
player_O = []

# Choose starting player
current_player = input("Who starts? (X/O): ").upper()
while current_player not in ['X', 'O']:
    current_player = input("Invalid. Choose X or O: ").upper()

# Game loop
for turn in range(9):
    clear()
    print_board(board)

    try:
        move = int(input(f"Player {current_player}, choose position (1-9): "))
    except ValueError:
        print("Invalid input!")
        continue

    if move not in board or board[move] in ['X', 'O']:
        print("Position already taken or invalid!")
        continue

    # Apply move
    board[move] = current_player

    if current_player == 'X':
        player_X.append(move)
        if check_win(player_X):
            clear()
            print_board(board)
            print("🎉 Player X Won!")
            break
        current_player = 'O'
    else:
        player_O.append(move)
        if check_win(player_O):
            clear()
            print_board(board)
            print("🎉 Player O Won!")
            break
        current_player = 'X'
else:
    clear()
    print_board(board)
    print("It's a DRAW!")