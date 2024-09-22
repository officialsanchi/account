import unittest
from classwork import generatePassword

class TestPasswordGenerator(unittest.TestCase):

    def test_default_password_length(self):
        password = generatePassword()
        self.assertEqual(len(password), 12)

    def test_custom_password_length(self):
        password = generatePassword(length=16)
        self.assertEqual(len(password), 16)

    def test_password_contains_word(self):
        password = generatePassword(use_words=True)
        self.assertGreaterEqual(len([char for char in password if char.isalpha()]), 5)

    def test_password_contains_number(self):
        password = generatePassword(use_numbers=True)
        self.assertGreaterEqual(len([char for char in password if char.isdigit()]), 2)

    def test_password_contains_special_char(self):
        password = generatePassword(use_special_chars=True)
        self.assertGreaterEqual(len([char for char in password if not char.isalnum()]), 2)

    def test_invalid_min_special_chars(self):
        with self.assertRaises(ValueError):
            generatePassword(min_special_chars=-1)
