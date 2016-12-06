"""
[2016-12-05] Challenge #294 [Easy] Rack management 1
https://tinyurl.com/dp-294-easy
"""
# path to enable1.txt
ENABLE1 = r"c:\code\GitHub\rdp\enable1.txt"
# worth table = {tile: [number of tiles, tile worth], ...}
WORTH_TABLE = {'?': [2, 0],
               'A': [9, 1],
               'B': [2, 3],
               'C': [2, 3],
               'D': [4, 2],
               'E': [12, 1],
               'F': [2, 4],
               'G': [3, 2],
               'H': [2, 4],
               'I': [9, 1],
               'J': [1, 8],
               'K': [1, 5],
               'L': [4, 1],
               'M': [2, 3],
               'N': [6, 1],
               'O': [8, 1],
               'P': [2, 3],
               'Q': [1, 10],
               'R': [6, 1],
               'S': [4, 1],
               'T': [6, 1],
               'U': [4, 1],
               'V': [2, 4],
               'W': [2, 4],
               'X': [1, 8],
               'Y': [2, 4],
               'Z': [1, 10]}

def scrabble(letter_tiles, word):
    """
    Determines whether word can be made using letter_tiles.

    Args:
        letter_tiles (str): string of letters and wildcard_sign signs
        word (str): input word

    Returns:
       bool: True for success, False otherwise.
    """
    wildcard_sign = "?"
    letter_list = list(letter_tiles)
    for letter in word:
        if letter in letter_list:
            letter_list.remove(letter)
        elif wildcard_sign in letter_list:
            letter_list.remove(wildcard_sign)
        else:
            return False
    return True

def longest(letter_tiles, words_list = ENABLE1):
    """
    Returns longest word from words_list that can be constructed
    using letters from letter_tiles. In case of tie returns first
    longest word found.

    Args:
        letter_tiles (str): string of letters and wildcard_sign signs
        words_list (file): list of words

    Returns:
        str: longest_word
    """
    longest_word = ""
    len_longest_word = len(longest_word)
    with open(words_list) as file:
        for line in file:
            line = line.strip()

            if len(line) < len_longest_word:
                continue

            if scrabble(letter_tiles, line):
                if len_longest_word < len(line):
                    longest_word = line
                    len_longest_word = len(line)
    return longest_word


def highest(letter_tiles, tile_worth = WORTH_TABLE):
    pass
        
        
        
if __name__ == '__main__':
    import unittest

    class TestFunctions(unittest.TestCase):
        def test_scrabble(self):
            self.assertTrue(scrabble("ladilmy", "daily"))
            self.assertFalse(scrabble("eerriin", "eerie"))
            self.assertTrue(scrabble("orrpgma", "program"))
            self.assertFalse(scrabble("orppgma", "program"))

        def test_scrabble_bonus_1(self):
            self.assertTrue(scrabble("pizza??", "pizzazz"))
            self.assertFalse(scrabble("piizza?", "pizzazz"))
            self.assertTrue(scrabble("a??????", "program"))
            self.assertFalse(scrabble("b??????", "program"))

        def test_longest_bonus_2(self):
            self.assertEqual(longest("dcthoyueorza"), "coauthored")
            self.assertEqual(longest("uruqrnytrois"), "turquois")
            self.assertEqual(longest("rryqeiaegicgeo??"), "greengrocery")
            self.assertEqual(longest("udosjanyuiuebr??"), "subordinately")
            self.assertEqual(longest("vaakojeaietg????????"), "ovolactovegetarian")

        def test_highest_bonus_3(self):
            self.assertEqual(highest("dcthoyueorza"), "zydeco")
            self.assertEqual(highest("uruqrnytrois"), "squinty")
            self.assertEqual(highest("rryqeiaegicgeo??"), "reacquiring")
            self.assertEqual(highest("udosjanyuiuebr??"), "jaybirds")
            self.assertEqual(highest("vaakojeaietg????????"), "straightjacketed")
            
    unittest.main()