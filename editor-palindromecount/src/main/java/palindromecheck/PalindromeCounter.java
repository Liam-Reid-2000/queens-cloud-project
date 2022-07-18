package palindromecheck;

/**
 * Count Palindromes
 */
public class PalindromeCounter {

    private String text;

    /**
     * Constructor
     *
     * @param text  Set text to the text
     *              passed in from the URL
     */
    public PalindromeCounter(String text) {
        this.text = text;
    }


    /**
     * Break the text string down into
     * an array of words
     *
     * @param text String passed in
     * @return     The words as an array
     * @throws PalindromeCounterException
     */
    private String[] getWords(String text) throws PalindromeCounterException {

        String processedText = PalindromeCounterUtil.getProcessedText(text);
        String[] wordsAsArray = PalindromeCounterUtil.getWordsAsArray(processedText);

        // If no words throw exception
        if (wordsAsArray.length < 1)
            throw new PalindromeCounterException("String empty");

        return wordsAsArray;
    }


    /**
     * Call off to the util class to get
     * the number of palindromes
     *
     * @return  Number of palindromes
     *          Returns -1 as answer if an error occurs
     */
    public int countPalindromes() {
        try {
            String[] words = getWords(text);
            int count = 0;
            // Check each word to see if its a palindrome
            for (String word : words) {
                String processedWord = PalindromeCounterUtil.removeSpecialChars(word);
                if (PalindromeCounterUtil.isPalindrome(processedWord) && (processedWord.length()>1))
                    count++;
            }
            return count;
        } catch (PalindromeCounterException e) {
            // An error has occurred
            return -1;
        }
    }
}
