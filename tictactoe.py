class TicTacToe:
    def __init__(self):
        pass

    def play(self):
        currentPlayer = "X"
        gameOver = False

        while not gameOver:
            self.print_board()
            row = int(input("Enter the row number (0-2): "))
            col = int(input("Enter the column number (0-2): "))

            if self.board[row][col] == " ":
                self.board[row][col] = currentPlayer
                currentPlayer = "O" if currentPlayer == "X" else "X"
            else:
                print("The cell is already occupied. Please choose another.")
        self.print_board()
    def main(self):
        pass


if __name__ == "__main__":
    game = TicTacToe()
    game.main()
    game.play()
