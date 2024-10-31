import unittest

from function_files import television
from  function_files.television import Television


class TestTelevision(unittest.TestCase):

    def test_that_television_exist(self):
       television = Television()

    def test_that_television_can_on(self):
        television = Television()
        self.assertTrue(television.turn_on())
    def test_that_television_can_off(self):
        television = Television()
        self.assertFalse(television.turn_off())

    def test_that_television_default_volume_is_zero(self):
        television = Television()
        self.assertTrue(television.turn_on())
        self.assertTrue(television.volume_up())


        get_channel = True

