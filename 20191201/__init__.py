def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20,30,70]))
    40.0
    """
    return sum(values)/len(values)

import doctest
doctest.testmod()

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20,30,70]),40)
        self.assertEqual(round(average([1,5,7]),1),5.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)
