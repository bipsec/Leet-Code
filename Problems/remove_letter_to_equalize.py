class Solution:
    def equalFrequency(self, word: str) -> bool:
        dupes = {}

        for item in word:
            if item in dupes:
                dupes[item] += 1
            else:
                dupes[item] = 1

        for char in dupes:
            dupes[char] -= 1
            if dupes[char] == 0:
                del dupes[char]

            if len(set(dupes.values())) == 1:
                return True
            dupes[char] = dupes.get(char, 0) + 1

        return False



s = Solution()
print(s.equalFrequency(word="abcc"))
print(s.equalFrequency(word="aazz"))
print(s.equalFrequency(word="ddaccb"))
print(s.equalFrequency(word="bac"))
print(s.equalFrequency(word="abbcc"))
