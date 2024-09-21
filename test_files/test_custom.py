import unittest
from classwork import custom


class TestCustom(unittest.TestCase):
    def test_custom_exist(self):
        self.assertTrue(custom.case_one)

    def test_that_input_has_a_lower_case(self):
        input = custom.case_two("chidinma")
        self.assertEqual(input, "chidinma")






