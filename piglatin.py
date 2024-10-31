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
        temp:str = ""
        if self.phrase[0] not in self.vowels:
            temp = self.phrase[1:] + self.phrase[0]

        if temp[-1] in self.vowels:
            translation = temp + "yay"
        elif temp[-1] is "y":
            translation = temp + "nay"
        else:
            translation = temp + "ay"
        return translation