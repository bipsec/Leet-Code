class Solution:
    def nextGreatestLetter(self, letters, target):

        for i in range(len(letters)):
            if target < letters[i]:
                return letters[i]

        return letters[0]


s = Solution()
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="c"))
print(s.nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))
