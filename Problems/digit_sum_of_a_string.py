class Solution:
    def digitSum(self, s: str, k: int) -> str:

        new_list = []
        count = 0

        for index in range(0, len(s), k):
            new_list.append(s[index: index + k])
            print(new_list)

        for i in new_list:
            print(i)
            for j in range(0, k):
                count += i[j]


s = Solution()
print(s.digitSum("11111222223", 3))
# print(s.digitSum("00000000", 3))
