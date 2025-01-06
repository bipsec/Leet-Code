class Solution:

    def counter(self, first_half, second_half):

        count_zero, count_one = 0, 0

        for i in range(len(first_half)):
            if first_half[i] == "0":
                count_zero += 1
        for j in range(len(second_half)):
            if second_half[j] == "1":
                count_one += 1
        return count_zero, count_one

    def maxScore(self, s: str) -> int:

        total_sum = 0

        start, end = 0, len(s) - 1
        res, val = "", ""

        while start < end:
            res += s[start]
            val = s[start + 1:]
            zeros, ones = self.counter(res, val)
            if zeros + ones > total_sum:
                total_sum = zeros + ones

            start += 1

        return total_sum


s = Solution()
print(s.maxScore(s="011101"))
print(s.maxScore(s="00111"))
print(s.maxScore(s="1111"))
