class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        pattern_map = {}
        used_words = set()

        for char, word in zip(pattern, words):
            if char not in pattern_map:
                if word in used_words:
                    return False
                pattern_map[char] = word
                used_words.add(word)
            else:
                if pattern_map[char] != word:
                    return False

        return True


s = Solution()
print(s.wordPattern(pattern="abba", s="dog cat cat dog"))
print(s.wordPattern(pattern="abba", s="dog cat cat fish"))
print(s.wordPattern(pattern="abba", s="dog dog dog dog"))
print(s.wordPattern(pattern="aaaa", s="dog cat cat dog"))
print(s.wordPattern(pattern="1", s="q"))
