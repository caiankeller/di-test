import unittest


def is_palindrome(input_string):
    clean_string = input_string.lower()
    length = len(clean_string)
    for i in range(length // 2):
        if clean_string[i] != clean_string[length - i - 1]:
            return False
    return True


class TestIsPalindrome(unittest.TestCase):

    def test_palindromes(self):
        self.assertTrue(is_palindrome("Amor a Roma"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("Not a palindrome"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))


if __name__ == '__main__':
    unittest.main()
