import unittest


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


class MyTestCase(unittest.TestCase):
    def test_２つの整数の和が計算できる(self):
        self.assertEqual(7, add(3, 4))
        self.assertEqual(3, add(1, 2))


class MyTestCase2(unittest.TestCase):
    def test_２つの整数の差が計算できる(self):
        self.assertEqual(1, subtract(4, 3))


if __name__ == "__main__":
    unittest.main()
