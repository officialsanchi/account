import unittest
from classwork import wordswap


class TestWordSwap(unittest.TestCase):

    def test_that_word_swap_exits(self):
        wordswap.swap()

    def test_that_word_swap(self):
        result = wordswap.main('abc','xyz')
        self.assertEqual('xycabz',result)
    def test_that_word_swap_case_two(self):
        result = wordswap.main('one','two')
        self.assertEqual('tweono',result)
    def test_that_word_swap_case_three(self):
        result = wordswap.main('four','five')
        self.assertEqual('fiurfove',result)





