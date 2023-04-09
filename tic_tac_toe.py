def display_board(board):
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
