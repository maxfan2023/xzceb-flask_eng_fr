import unittest

from translator import english_to_french,french_to_english

class TestEnglist_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), '') # test when 2 is given as input the output is 4.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when 3.0 is given as input the output is 9.0.
 

class TestFrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None), '') # test when 2 is given as input the output is 4.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
 
unittest.main()