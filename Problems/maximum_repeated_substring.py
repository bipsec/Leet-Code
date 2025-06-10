class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0

        start, end = len(word), len(sequence) - 1

        for i in range(len(sequence)):
            while start <= end:
                print(sequence[i: start])
                if sequence[i: start] == word:
                    count += 1
                start += len(word)

        return count


s = Solution()
print(s.maxRepeating(sequence="ababc", word="ab"))
print(s.maxRepeating(sequence="ababc", word="ba"))
# print(s.maxRepeating(sequence="ababc", word="ac"))
# print(s.maxRepeating(sequence="abahfiuhwrhfawenfbc", word="hh"))
# print(s.maxRepeating(sequence="aaabaaaabaaabaaaabaaaabaaaabaaaaba", word="aaaba"))
