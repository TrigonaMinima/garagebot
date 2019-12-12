import unittest

from context import text_utils


class TestTextUtilFunctions(unittest.TestCase):
    """
    Tests all the API methods
    """

    def test_valid_word(self):
        invalid_words = ["", "1", "11", "a", "a1", "1a", "a1b", "a_b"]
        for word in invalid_words:
            print(word)
            result = text_utils.valid_word(word)
            expected = 0
            self.assertEqual(result, expected)

        valid_words = ["ab", "Abc", "sdsd@bs"]
        for word in valid_words:
            result = text_utils.valid_word(word)
            expected = 1
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
