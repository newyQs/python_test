import unittest
from fizzbuzz import FizzBuzz


class FizzBuzzTestCase(unittest.TestCase):
    def test_普通数字_返回它本身(self):
        assert FizzBuzz.of(1) == '1'

    def test_被3整除的数字_返回Fizz(self):
        assert FizzBuzz.of(3) == 'Fizz'

    def test_被5整除的数字_返回Fizz(self):
        assert FizzBuzz.of(5) == 'Buzz'

    def test_同时被3和5整除的数字_返回FizzBuzz(self):
        assert FizzBuzz.of(15) == 'FizzBuzz'

    def test_数字等于0_抛出异常(self):
        with self.assertRaises(Exception):
            FizzBuzz.of(0)


if __name__ == '__main__':
    unittest.main()
