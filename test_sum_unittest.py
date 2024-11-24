import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "should be 6")

if __name__=='__Main__':
    unittest.main()
    # Executing this test will show one sucess and one failure
    # test_sum passed while test_sum_tuple does not