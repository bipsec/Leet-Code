class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):

            return False
        else:
            for i in range(len(s)):
                for j in range(len(goal)):
                    if s[i] in goal:
                        if s[i] != goal[j]:
                            pass


# this problem is a little bit difficult for me, I guess.


s = Solution()
print(s.buddyStrings(s="ab", goal="ba"))
print(s.buddyStrings(s="ab", goal="ab"))
print(s.buddyStrings(s="aa", goal="aa"))
print(s.buddyStrings(s="aaaaaaabc", goal="aaaaaaacb"))

# need to solve this, it's a fun problem and the most easy one I think but tricky~!
