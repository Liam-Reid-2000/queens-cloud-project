require 'test/unit/assertions'
require 'test/unit'
include Test::Unit::Assertions
require_relative 'averageWordLength'
include AverageWordLengthMethods


ENV['ENV_ENV'] = 'test'

class MethodTest < Test::Unit::TestCase
    
    def testExecute
        assert_equal 3, execute("cat"), "Average should be 3"
        assert_equal 4, execute("Cloud cat"), "Average should be 4"
        assert_equal 4, execute("Four Four Four"), "Average should be 4"
        assert_equal 4, execute("Four, Four, Four,"), "Average should be 4"
        assert_equal -1, execute(""), "Average should be -1 (Error)"
    end

    def testProcessText
        assert_equal "Hello", process_text("Hello")
        assert_equal " Hello ", process_text("%20Hello%20")
        assert_equal "Hello", process_text("!Hello!")
        assert_equal "Hello", process_text("=Hello@")
        assert_equal "Hello", process_text("/Hello%")
    end
end