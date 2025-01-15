class Solution:

    def shift_char(self, arr, shift):
        if len(arr) == 1:
            arr = (ord(arr) - ord('a') + shift) % 26 + ord('a')
            return chr(arr)
        else:
            chars = ""
            for item in arr:
                shifted = (ord(item) - ord('a') + shift) % 26 + ord('a')
                chars += chr(shifted)
            return chars

    def shiftingLetters(self, s: str, shifts) -> str:

        n = len(shifts)
        for i in range(n - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        res = ""
        for i in range(len(s)):
            char = s[i]
            res += self.shift_char(char, shifts[i])

        return res


s = Solution()
print(s.shiftingLetters(s="abc", shifts=[3, 5, 9]))
print(s.shiftingLetters(s="bad", shifts=[10, 20, 30]))
