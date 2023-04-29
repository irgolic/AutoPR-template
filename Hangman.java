import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class Hangman {

    public static void main(String[] args) {
        final String ANSI_RESET = "\u001B[0m";
        final String ANSI_RED = "\u001B[31m";
        final String ANSI_GREEN = "\u001B[32m";
        final String ANSI_YELLOW = "\u001B[33m";
        final String ANSI_BLUE = "\u001B[34m";
        final String ANSI_PURPLE = "\u001B[35m";
        final String ANSI_CYAN = "\u001B[36m";
        Scanner scanner = new Scanner(System.in);
        boolean playing = true;
        
        while (playing) {
            // Begin game
            boolean roundCompleted = playGame(scanner);
            
            // Ask user to play again
            System.out.print("Do you want to play again? (yes/no): ");
            String userChoice = scanner.next().toLowerCase();
            if (!userChoice.equals(ANSI_YELLOW + "yes" + ANSI_RESET)) {
                playing = false;
        private static final String[] words = {"apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"};
            }
        }
    }
    
    public static boolean playGame(Scanner scanner) {
        // TODO: Implement the game logic
        String word = getRandomWord();
        StringBuilder guessedWord = new StringBuilder(word.replaceAll(".", "_"));
        int attemptsLeft = 6;
        boolean guessed = false;
        
        while (attemptsLeft > 0) {
            System.out.println("Word: " + guessedWord);
            System.out.print("Guess a letter: ");
            char letter = scanner.next().toLowerCase().charAt(0);

            if (word.indexOf(ANSI_BLUE + letter + ANSI_RESET) >= 0) {
                for (int i = 0; i < word.length(); i++) {
                    if (word.charAt(i) == letter) {
                        guessedWord.setCharAt(i, letter);
                    }
                }
                System.out.println(ANSI_GREEN + "Correct guess!" + ANSI_RESET);

                if (!guessedWord.toString().contains("_")) {
                    guessed = true;
                    break;
                }
            } else {
                attemptsLeft--;
                System.out.println("Incorrect guess! You have " + attemptsLeft + " attempts left.");
                System.out.println(ANSI_RED + "Incorrect guess! You have " + attemptsLeft + " attempts left." + ANSI_RESET);
            }
        }
        System.out.println(guessed ? ANSI_GREEN + "Congratulations, you guessed the word!" + ANSI_RESET : ANSI_RED + "Sorry, you ran out of attempts. The word was " + word + "." + ANSI_RESET);
        return guessed;
    }
    private static String getRandomWord() {
        Random random = new Random();
        int index = random.nextInt(words.length);
        return words[index];
    }
}
