class TicTacToe:
    def __init__(self):
        pass

    def play(self):
        currentPlayer = "X"
        gameOver = False

        while not gameOver:
                if self.check_winner():
                    print("Player", currentPlayer, "wins!")
                    gameOver = True
                    break
            self.print_board()
            row = int(input("Enter the row number (0-2): "))
            col = int(input("Enter the column number (0-2): "))

            if self.board[row][col] == " ":
                self.board[row][col] = currentPlayer
                currentPlayer = "O" if currentPlayer == "X" else "X"
            else:
                print("The cell is already occupied. Please choose another.")
        self.print_board()
    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def main(self):
        pass


if __name__ == "__main__":
    game = TicTacToe()
    game.main()
    game.play()
