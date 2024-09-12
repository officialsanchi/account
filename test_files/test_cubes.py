import unittest
from function_files import cubes


class TestThatNumberCanMultiplyItselfThreeTimes(unittest.TestCase):

    def test_That_Number_Can_Multiply_Itself_Three_Times_exist(self):
        cubes.that_Number_Can_Multiply_Itself_Three_Times({1,2,3,4,5})



    def test_That_Number_Can_Multiply_Itself_Three_Times_function_return_dict(self):
        actual = cubes.that_Number_Can_Multiply_Itself_Three_Times([1,2,3,4,5])
        expected = {1:1,2:8,3:27,4:64,5:125}
        self.assertEqual(actual,expected)