import java.util.Scanner;

public class Hangman {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean playing = true;
        
        while (playing) {
            // Begin game
            boolean roundCompleted = playGame(scanner);
            
            // Ask user to play again
            System.out.print("Do you want to play again? (yes/no): ");
            String userChoice = scanner.next().toLowerCase();
            if (!userChoice.equals("yes")) {
                playing = false;
            }
        }
    }
    
    public static boolean playGame(Scanner scanner) {
        // TODO: Implement the game logic
        return false;
    }
}
