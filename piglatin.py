class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    @classmethod
    def PigLatin(cls, phrase:str):
        return cls(phrase)

    def get_phrase(self) -> str:
        return self.phrase
        
    def translate(self) -> str:
        pass