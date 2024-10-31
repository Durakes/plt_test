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
        temp:str = self.get_phrase()
        while temp[0] not in self.vowels:
            consonant = temp[0]
            temp = temp[1:] + consonant

        if temp[-1] in self.vowels:
            translation = temp + "yay"
        elif temp[-1] is "y":
            translation = temp + "nay"
        else:
            translation = temp + "ay"
        return translation