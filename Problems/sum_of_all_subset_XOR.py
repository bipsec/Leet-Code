class Solution:
    def subsetXORSum(self, nums) -> int:
        XOR_ = [[], ]

        for item in nums:
            XOR_ += [sub + [item] for sub in XOR_]

        print(XOR_)


s = Solution()
print(s.subsetXORSum([1, 3]))
