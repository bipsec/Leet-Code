class Solution:
    def countSeniors(self, details):
        count = 0
        for item in details:
            if int(item[-4:-2]) > 60:
                count += 1
        return count


s = Solution()
print(s.countSeniors(details=["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
print(s.countSeniors(details=["1313579440F2036", "2921522980M5644"]))
print(s.countSeniors(details=["5612624052M0130", "5378802576M6424", "5447619845F0171", "2941701174O9078"]))
