import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

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
        private static final String[] words = {"apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"};
            }
        }
    }
    
    public static boolean playGame(Scanner scanner) {
        // TODO: Implement the game logic
        return false;
    }
    private static String getRandomWord() {
        Random random = new Random();
        int index = random.nextInt(words.length);
        return words[index];
    }
}
