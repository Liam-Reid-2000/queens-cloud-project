package palindromecheck;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PalindromeCounterTest {

    private PalindromeCounter test;

    @Test
    public void countPalindromesTest() {
        String text = "This sentence had two palindromes, mom and kayak.";
        test = new PalindromeCounter(text);
        assertEquals(2, test.countPalindromes());

        text = "This sentence had three palindromes, mom, kayak and racecar.";
        test = new PalindromeCounter(text);
        assertEquals(3, test.countPalindromes());

        text = "This sentence had no palindromes.";
        test = new PalindromeCounter(text);
        assertEquals(0, test.countPalindromes());
    }

}