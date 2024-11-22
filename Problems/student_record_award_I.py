class Solution:
    def checkRecord(self, s: str) -> bool:

        count = 0
        l_count = 0
        for item in range(len(s) - 1, -1, -1):

            if s[item] == "A":
                count += 1
                l_count = 0
                if count >= 2:
                    return False
            elif s[item] == "L":
                l_count += 1
                if l_count >= 3:
                    return False
            else:
                l_count = 0

        return True


s = Solution()
print(s.checkRecord(s="PPALLP"))
print(s.checkRecord(s="PPALLL"))
print(s.checkRecord(s="PPALLPPAAPPP"))
print(s.checkRecord(s="AA"))
print(s.checkRecord(s="LALL"))
