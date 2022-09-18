import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('hello'), 'bonjour')   
        self.assertNotEqual(english_to_french('hello'), 'hello')  
       
class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('bonjour'), 'hello')   
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')

class TestNull(unittest.TestCase):
    def test2(self):
        self.assertIsNone(french_to_english('')) 
        self.assertIsNone(english_to_french('')) 

unittest.main()