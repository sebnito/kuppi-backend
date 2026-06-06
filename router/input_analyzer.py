from pythainlp.tokenize import word_tokenize

class InputAnalyzer:

    '''Class to analyze user input and extract relevant information.'''

    #non-static variable
    def __init__(self):
        pass

    # Thai sentences --> list of words using pythainlp
    def tokenize(self, text: str) -> list[str]:
        tokens = word_tokenize(text, engine="newmm")
        return tokens
    
    
