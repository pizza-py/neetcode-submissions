class WordDictionary:

    def __init__(self):
        self.children = dict()
        self.terminator = False
        self.isWildCard = False

    def addWord(self, word: str) -> None:
        if not word:
            self.terminator = True
            return

        if word[0] not in self.children:
            self.children[word[0]] = WordDictionary()
        
        self.children[word[0]].addWord(word[1:])
        
        

    def search(self, word: str) -> bool:
        if not word and self.terminator:
            return True
        elif not word:
            return False

        if word[0] == ".":
            res = False
            for child in self.children.values():
                res |= child.search(word[1:])
            return res

        if word[0] not in self.children:
            return False
        
        return self.children[word[0]].search(word[1:])
        
