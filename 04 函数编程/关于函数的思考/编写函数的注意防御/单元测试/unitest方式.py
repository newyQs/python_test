import unittest


def sum_numbers(x, y):
    return x + y


class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_numbers(3, 4), 7)
