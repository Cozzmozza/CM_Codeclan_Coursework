import unittest

from src.fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz__divisible_by_3_returns_fizz(self):
        self.assertEqual('Fizz', fizz_buzz(3))
    
    def test_fizz_buzz__divisible_by_5_returns_buzz(self):
        self.assertEqual('Buzz', fizz_buzz(5))
    
    def test_fizz_buzz__divisible_by_3_and_5_returns_FizzBuzz(self):
        self.assertEqual('FizzBuzz',fizz_buzz(15))

    def test_fizz_buzz__otherwise_returns_input(self):
        self.assertEqual(7, fizz_buzz(7))


# Tests:
# return 'Fizz' if number is divisible by 3
# return 'Buzz' if number is divisible by 5
# return 'FizzBuzz' if number is divisible by 3 and 5
# return the input as a string otherwwise e.g if we input 7, return 7

# Write a test, get it to pass, then write the next test