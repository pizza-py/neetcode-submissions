class PrefixTree:

    def __init__(self):
        self.letterToNode = dict()
        self.terminator = False
        

    def insert(self, word: str) -> None:
        if word == "":
            self.terminator = True
            return

        if word[0] not in self.letterToNode:
            self.letterToNode[word[0]] = PrefixTree()
        self.letterToNode[word[0]].insert(word[1:])
            

    def search(self, word: str) -> bool:
        if word == "" and self.terminator:
            return True
        elif word == "" and not self.terminator:
            return False

        if word[0] not in self.letterToNode:
            return False
        return self.letterToNode[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True

        if prefix[0] not in self.letterToNode:
            return False
        return self.letterToNode[prefix[0]].startsWith(prefix[1:])
        
        