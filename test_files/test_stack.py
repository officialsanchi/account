import unittest
from dataStructure import stack
from dataStructure.stack import stack_is_empty, stack_push, stack_count


class StackTests(unittest.TestCase):

    def test_that_Stack_exists(self):
        self.assertTrue(stack)

    def test_that_Stack_is_empty(self):
        self.assertTrue(stack_is_empty())

    def test_that_stack_can_push_values(self):
        stack_push("chidinma")
        self.assertEqual(1, stack_count())
        self.assertFalse(stack_is_empty())

    def test_that_stack_is_not_empty(self):
        stack_push("chidinma")
        self.assertFalse(stack_is_empty())

    def test_that_push_and_pop_values(self):
        stack_push("chidinma")
        stack_pop()
        self.assertEqual(0, stack_count())

    def test_that_pop_when_stack_is_empty(self):
        stack_pop()
        self.assertEqual(0, stack_count())

    def test_that_push_X_and_pop_X(self):
        stack_push("chidinma")
        self.assertEqual(stack_pop(),"chidinma")