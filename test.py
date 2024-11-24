import unittest

from my_sum import sum
from fractions import fraction 

class TestSum(unittest.Testcase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [ Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__=='__Main__':
    unittest.main()
# this example imports sum() from my_sum,
# defines a new test case class called TestSum
# and defines a test method test_list_int()

# when running python -m unittest test, message shows NO TESTS RAN
# whe running pythom -m unittest -v test, message  shows NO TESTS RAN
# when running python -m unittest discover, message shows NO TESTS RAN
# when running python -m unittest discover -s tests, message shows import error: Start directory is not importable 
# when running python -m unittest discover -s tests -t src, message shows Start directory is not importable 


