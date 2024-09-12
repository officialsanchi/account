import unittest
from classwork import count
from classwork.count import word_pass_in_parameter_can_be_counted


class TestCount(unittest.TestCase):
    def test_count_function_can_return_dict(self):
        actual = word_pass_in_parameter_can_be_counted("obioma")
        expected = {'o':2,'b':1,'i':1,'m':1,'a':1}
        self.assertEqual(actual, expected)






