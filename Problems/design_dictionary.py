class WordDictionary:

    def __init__(self):
        self.dictionary = dict()

    def addWord(self, word: str) -> None:
        if word not in self.dictionary.keys():
            self.dictionary[word] = 1

    def search(self, word: str) -> bool:
        for key, val in self.dictionary.items():
            pass





# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)