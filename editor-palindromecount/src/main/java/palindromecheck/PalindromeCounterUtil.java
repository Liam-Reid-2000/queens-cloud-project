package palindromecheck;

/**
 * Static utility class
 */
public class PalindromeCounterUtil {

    /**
     * Replace %20 in text with a space
     *
     * @param text  passed in from url
     * @return      the processed text
     */
    public static String getProcessedText(String text) {
        String processedText = text
                .replace("%20", " ")
                .replace("=", " ");
        return processedText;
    }


    /**
     * Split the words on spaces
     *
     * @param text  text
     * @return      array of words from text
     */
    public static String[] getWordsAsArray(String text) {
        String[] wordsArrayList = text
                .split(" ");
        return wordsArrayList;
    }


    /**
     * Remove special characters from words
     *
     * @param text  word
     * @return      word without any special chars
     */
    public static String removeSpecialChars(String text) {
        String textNoSpecialChars = text
                .replaceAll("[^a-zA-Z0-9]", "");
        return textNoSpecialChars;
    }


    /**
     * Check if input is a palindrome
     *
     * @param input word
     * @return      if word is palindrome or not
     */
    public static boolean isPalindrome(String input) {

        // Return false if for example the letter 'a'
        // is passed to here
        if (input.length() <=1)
            return false;

        // Convert string to lower case
        String inputLowerCase = input.toLowerCase();

        // Reverse string
        String reversed = "";
        for (int i = inputLowerCase.length() -1; i>=0; i--)
            reversed = reversed + inputLowerCase.charAt(i);

        // Compare
        if (reversed.equals(inputLowerCase))
            return true;

        // Return false if they do not match
        return false;
    }
}
