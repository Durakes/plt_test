class PigLatin:
    def __init__(self, phrase: str):
        self.vowels = ["a", "e", "i", "o", "u"]
        self.phrase = phrase

    @classmethod
    def PigLatin(cls, phrase:str):
        return cls(phrase)

    def get_phrase(self) -> str:
        if self.phrase is "":
            return "nil"
        return self.phrase
        
    def translate(self) -> str:
        translation:str = ""
        if self.phrase[-1] in self.vowels:
            translation = self.phrase + "yay"
        elif self.phrase[-1] is "y":
            translation = self.phrase + "nay"
        else:
            translation = self.phrase + "ay"
        return translation