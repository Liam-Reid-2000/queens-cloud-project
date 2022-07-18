package palindromecheck;

public class PalindromeCounterException extends Exception {

    /**
     * Exception if something goes wrong
     * with palindrome count
     *
     * @param message
     */
    public PalindromeCounterException(String message) {
        super(message);
    }
}
