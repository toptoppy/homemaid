import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_input_3_should_get_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result,'Fizz')

    def test_input_6_should_get_fizz(self):
        result = fizzbuzz(6)
        self.assertEqual(result,'Fizz')

    def test_input_15_should_get_fizzbizz(self):
        result = fizzbuzz(15)
        self.assertEqual(result, 'FizzBuzz')
    
    def test_input_450_should_get_fizzbizz(self):
        result = fizzbuzz(450)
        self.assertEqual(result, 'FizzBuzz')

# comment this for run pytest
# unittest.main()