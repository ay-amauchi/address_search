import unittest
from search_address import search_address


class MyTestCase(unittest.TestCase):
    def test_郵便番号から住所を取得できる_0287111(self):
        num = "0287111"
        address = search_address(num)

        expect = "岩手県八幡平市大更"

        self.assertEqual(expect, address)


class MyTestCase2(unittest.TestCase):
    def test_郵便番号から住所を取得できる_0287302(self):
        num = "0287302"
        address = search_address(num)

        expect = "岩手県八幡平市八幡平温泉郷"

        self.assertEqual(expect, address)


if __name__ == "__main__":
    unittest.main()
