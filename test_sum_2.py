def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__Main__":
    test_sum()
    test_sum_tuple()
    print("Everything Passed")

# FAIL: test_sum_tuple (__main__.TestSum)Traceback (most recent call last):
#File "test_sum_unittest.py", line 9, in test_sum_tuple
#self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
# AssertionError: Should be 6 - this means the result of test_sum_tuple did not pass
# because it does not equal to 6, it is equal to 5