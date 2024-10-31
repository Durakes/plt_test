import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_initialize_translator(self):
        translator:PigLatin = PigLatin.PigLatin("hello world")

        self.assertEqual("hello world",translator.get_phrase())