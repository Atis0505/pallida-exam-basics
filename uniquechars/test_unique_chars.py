import unittest
from unique_chars import unique_characters

class TestUnique_Chars(unittest.TestCase):

    def test_one_letter(self):
        self.assertEqual(unique_characters("a"), ['a'])


    def test_empty_input(self):
        self.assertFalse(unique_characters(""))

    
    def test_no_unique_letter_in_word(self):
        self.assertEqual(unique_characters("aabb"), -1)

    
if __name__ == "__main__":
    unittest.main()