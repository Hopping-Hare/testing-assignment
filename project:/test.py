import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        ## test that it can sum a list of integers
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        ## test that it can sum a list of fractions
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()


## The test results are to tell us whether the code ran successfully or not.
## If it didn't, the test will fail and it'll tell us where it failed so
## we can go back and fix it. When we run the test again, it should pass
## if we fixed the problem properly.
