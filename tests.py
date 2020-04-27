import unittest
from my_sum import sum1, power

#  target = __import__("my_sum.py")
#  sum1 = target.sum1
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum1(data)
        self.assertEqual(result, 6)


def test_my_function(benchmark):
    result = benchmark(power(4))
    assert result == 16


if __name__ == "__main__":
    unittest.main()
