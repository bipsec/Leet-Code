from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        dupes = {}
        for i in range(len(deck)):
            if deck[i] in dupes:
                dupes[deck[i]] += 1
            else:
                dupes[deck[i]] = 1
        val = list(dupes.values())

        if gcd(*val) > 1:
            return True
        return False


s = Solution()
# print(s.hasGroupsSizeX(deck=[1, 2, 3, 4, 4, 3, 2, 1]))
# print(s.hasGroupsSizeX(deck=[1, 1, 1, 2, 2, 2, 3, 3]))
# print(s.hasGroupsSizeX(deck=[1]))
# print(s.hasGroupsSizeX(deck=[1, 2]))
# print(s.hasGroupsSizeX(deck=[1, 1, 1, 1, 1, 1, 1, 11]))
# print(s.hasGroupsSizeX(deck=[1, 1, 0]))
print(s.hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
