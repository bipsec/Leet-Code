class Solution:
    def firstPalindrome(self, words) -> str:
        dupes = []
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                dupes.append(words[i])

        return dupes[0] if len(dupes) >= 1 else ""


s = Solution()
print(s.firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"]))
print(s.firstPalindrome(words=["abc", "car", "adav", "racecarv", "coole"]))
print(s.firstPalindrome(words = ["notapalindrome","racecar"]))
