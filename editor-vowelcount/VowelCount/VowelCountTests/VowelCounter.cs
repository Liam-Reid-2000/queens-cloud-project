namespace VowelCount.Tests
{
    public class VowelCounter
    {
        public static int CountVowels(string textToCheck)
        {
            int count = 0;
            foreach (char c in textToCheck)
            {
                if ((c == 'a') || (c == 'e') || (c == 'i') || (c == 'o') || (c == 'u') ||
                    (c == 'A') || (c == 'E') || (c == 'I') || (c == 'O') || (c == 'U'))
                {
                    count++;
                }
            }
            return count;
        }
    }
}