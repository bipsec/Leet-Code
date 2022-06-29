from itertools import combinations
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        count = 0

        subsets = []
        subsets.append([])
        for num in s:
            for i in range(len(subsets)):
                aset = list(subsets[i])
                aset.append(num)
                subsets.append(aset)
        # return subsets
        print(subsets)

        for i in words:
            if i in subsets:
                count += 1
        return count


s = Solution()
print(s.numMatchingSubseq("abc",["a","bb","acd","ace"]))