import unittest
from classwork import middle


class TestThatWordCanBeAddedAtTheMiddle(unittest.TestCase):
    def test_that_middle_exist(self):
        middle.main()
    def test_that_word_can_be_added(self):
        result = middle.add_words('helloo','ce')
        self.assertTrue( 'helceloo',result)
    def test_that_word_can_be_added_two(self):
        result = middle.add_words('joy','ce')
        self.assertTrue( 'joyce',result)
    def test_that_word_can_be_added_three(self):
        result = middle.add_words('manner','ce')
        self.assertTrue( 'mancener',result)
    def test_that_word_can_be_added_four(self):
        result = middle.add_words('two','ce')
        self.assertTrue( 'twonce',result)
