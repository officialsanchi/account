import unittest
from classwork import alphabate


class TestForUpperAndLowerCase(unittest.TestCase):
    def test_alphabate_exists(self):
        alphabate.case_one()
    def test_that_upper_case_and_lower_case_work(self):
        value = alphabate.case_two("seMiCOLOn")
        self.assertEqual("seMiCOLOn", value)





