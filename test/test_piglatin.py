import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_initialize_translator(self):
        translator:PigLatin = PigLatin.PigLatin("hello world")

        self.assertEqual("hello world",translator.get_phrase())
    
    def test_translate_empty_string(self):
        translator:PigLatin = PigLatin("")

        self.assertEqual("nil",translator.get_phrase())
