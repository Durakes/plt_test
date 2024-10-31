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

    def test_translate_start_consonant(self):
        translator:PigLatin = PigLatin("hello")
        translation = translator.translate()
        self.assertEqual("ellohay",translation)

    def test_translate_more_cosonants_start(self):
        translator:PigLatin = PigLatin("known")
        translation = translator.translate()
        self.assertEqual("ownknay",translation)

    def test_translate_more_words_space(self):
        translator:PigLatin = PigLatin("hello world")
        translation = translator.translate()
        self.assertEqual("ellohay orldway",translation)

    def test_translate_more_words_composite(self):
        translator:PigLatin = PigLatin("well-being")
        translation = translator.translate()
        self.assertEqual("ellway-eingbay",translation)

    def test_translate_punctuation(self):
        translator:PigLatin = PigLatin("hello world!")
        translation = translator.translate()
        self.assertEqual("ellohay orldway!",translation)
    
    def test_translate_wrong_punctuation(self):
        translator:PigLatin = PigLatin("hello world!+")
        self.assertRaises(PigLatinError,translator.translate)