def display_board(board):
    # Code for displaying the board
    pass

def check_winner(board):
    # Code for checking the winner
    pass

def update_board(board, row, col, player):
    board[row][col] = player
    return board

def get_user_input(player):
    row = int(input(f"Player {player}, enter the row (0-2): "))
    col = int(input(f"Player {player}, enter the column (0-2): "))
    return row, col

def is_valid_move(board, row, col):
    return board[row][col] == " "

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while not check_winner(board) and not is_board_full(board):
        display_board(board)
        row, col = get_user_input(current_player)

        if not is_valid_move(board, row, col):
            print("Invalid move, please try again.")
            continue

        update_board(board, row, col, current_player)

        if check_winner(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break
        else:
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
def display_board(board):
    # Code for displaying the board goes here
    pass

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    display_board(board)

    # Gameplay loop goes here
    pass

if __name__ == "__main__":
    main()
def display_board(board):
def display_board(board):
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell or " ", end="|")
        print("\n" + "-" * 5)


    board = [["" for _ in range(3)] for _ in range(3)]
    display_board(board)

    pass

def check_winner(board):
    pass

def handle_user_input(player):
    pass

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(board)
        row, col = handle_user_input(current_player)
        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print(f"{winner} is the winner!")
            game_over = True
        elif all([cell != ' ' for row in board for cell in row]):
            print("It's a tie!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
