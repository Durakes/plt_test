from error import PigLatinError
class PigLatin:
    def __init__(self, phrase: str):
        self.vowels = ["a", "e", "i", "o", "u"]
        self.punctuation_marks = [".", ",", ":",";" ,"'", "?", "!", "(", ")"]
        self.phrase = phrase

    @classmethod
    def PigLatin(cls, phrase:str):
        return cls(phrase)

    def get_phrase(self) -> str:
        if self.phrase is "":
            return "nil"
        return self.phrase
        
    def translate(self) -> str:
        words = self.phrase.split()
        translation:str = ""

        for i, word in enumerate(words):
            if '-' in word:
                temp_words = word.split("-")
                translation = self.modify_words(temp_words, "-")
            else:
                translation = self.modify_words(words," ")
        return translation
    
    def modify_words(self, words, modifier:str) -> str:
        translation: str = "" 
        # Only testing the examples
        for i, word in enumerate(words):
            temp:str = word
            punctuation = ""
            position = -1
            for x in temp:
                if not x.isalpha() and x not in self.punctuation_marks:
                    raise PigLatinError
                elif x in self.punctuation_marks:
                    punctuation = x
                    position = temp.find(x)
                    temp = temp.replace(punctuation,"")
            while temp[0] not in self.vowels:
                consonant = temp[0]
                temp = temp[1:] + consonant

            if temp[-1] in self.vowels:
                translation += temp + "yay"
            elif temp[-1] is "y":
                translation += temp + "nay"
            else:
                translation += temp + "ay"

            if i+1 < len(words):
                translation += modifier

            # Doesn't support some specific cases
            if position == 0:
                translation = punctuation + translation
            else:
                translation = translation + punctuation
        return translation