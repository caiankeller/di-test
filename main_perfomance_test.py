import unittest


def is_palindrome(input_string):
    clean_string = input_string.lower()
    left = 0
    right = len(clean_string) - 1

    while left < right:
        if clean_string[left] != clean_string[right]:
            return False
        left += 1
        right -= 1
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
