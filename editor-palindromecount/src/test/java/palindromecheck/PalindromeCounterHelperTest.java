package palindromecheck;

import org.junit.Test;

import static org.junit.Assert.*;

public class PalindromeCounterHelperTest {

    private PalindromeCounterUtil test = new PalindromeCounterUtil();

    @Test
    public void getProcessedTextTest() {
        String unprocessedText = "Hello%20this%20is%20what%20url%20looks%20like";
        String expectedText = "Hello this is what url looks like";
        String processedText = test.getProcessedText(unprocessedText);
        assertEquals(expectedText, processedText);
    }

    @Test
    public void getWordsAsArrayTest() {
        String text = "one two three four";
        String[] expectedArray = { "one", "two", "three", "four" };
        String[] array = test.getWordsAsArray(text);
        assertEquals(expectedArray[0], array[0]);
        assertEquals(expectedArray[1], array[1]);
        assertEquals(expectedArray[2], array[2]);
        assertEquals(expectedArray[3], array[3]);
    }

    @Test
    public void removeSpecialCharsTest() {
        assertEquals("Hello", test.removeSpecialChars("Hello!"));
        assertEquals("Cloud", test.removeSpecialChars("<Cloud>"));
        assertEquals("Palindrome", test.removeSpecialChars("\"Palindrome\""));
        assertEquals("Dog", test.removeSpecialChars("%Dog@=*"));
        assertEquals("Cat", test.removeSpecialChars("!Cat()"));
    }

    @Test
    public void isPalindromeTest() {
        assertTrue(test.isPalindrome("kayak"));
        assertTrue(test.isPalindrome("racecar"));
        assertTrue(test.isPalindrome("mom"));
        assertTrue(test.isPalindrome("Dad"));

        assertFalse(test.isPalindrome("Dog"));
        assertFalse(test.isPalindrome("cat"));
        assertFalse(test.isPalindrome("yoyo"));
        assertFalse(test.isPalindrome("a"));
    }
}