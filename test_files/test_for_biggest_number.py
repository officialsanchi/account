import unittest
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

class TestBiggestnumber(unittest.TestCase):

    def test_that_biggest_number_function_exist(self):
        biggestnumber.biggest_number("23956")

    def test_biggest_function_returns_biggest_number(self):
        result = biggestnumber.biggest_number("23956")
        self.assertEqual(result, 9)

