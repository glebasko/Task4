import unittest
import doctest
import division

class TestDivision(unittest.TestCase):
    def test_divisionByZero(self):
         with self.assertRaises(ValueError):
             division.divide(5, 0)

    def test_overflow(self):
        with self.assertRaises(OverflowError):
             division.divide(1e100, 1)

    def test_simpleDivision(self):
        self.assertEqual(division.divide(500, 10), 50.0)

    def test_negativeDivision(self):
        self.assertEqual(division.divide(-400, 20), -20.0)

    def test_floatDivision(self):
        self.assertEqual(division.divide(1.5, 0.23), 6.521739130434782)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(division))
    return tests

if __name__ == '__main__':
    unittest.main()
