using System;
using Xunit;

namespace VowelCount.Tests
{
    public class VowelCounterTests
    {
        [Fact]
        public void CountVowelsTest()
        {
            Assert.True(5 == VowelCounter.CountVowels("a e i o u"));
            Assert.True(5 == VowelCounter.CountVowels("A E I O U"));
            Assert.True(2 == VowelCounter.CountVowels("Cloud"));
            Assert.True(2 == VowelCounter.CountVowels("CLOUD"));
            Assert.True(2 == VowelCounter.CountVowels("CLOuD"));
            Assert.True(4 == VowelCounter.CountVowels("Cloud Project"));
        }
    } // https://www.pluralsight.com/guides/testing-.net-core-apps-with-visual-studio-code
}