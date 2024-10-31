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

    def test_translate_with_end_y(self):
        translator:PigLatin = PigLatin("any")
        translation = translator.translate()
        self.assertEqual("anynay",translation)

    def test_translate_with_end_vowal(self):
        translator:PigLatin = PigLatin("apple")
        translation = translator.translate()
        self.assertEqual("appleyay",translation)

    def test_translate_with_end_consonant(self):
        translator:PigLatin = PigLatin("ask")
        translation = translator.translate()
        self.assertEqual("askay",translation)