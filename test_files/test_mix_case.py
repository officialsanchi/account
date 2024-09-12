import unittest
from classwork import mixCase



class TestMixCase(unittest.TestCase):
    def test_that_mix_case_exist(self):
        mixCase.caseone()

    def test_that_mix_case_can_take_upper_and_lower_case_and_upper_case_first(self):
        mixCase.