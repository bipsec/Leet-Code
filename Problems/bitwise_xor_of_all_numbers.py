class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        len1 = len(nums1) % 2
        len2 = len(nums2) % 2
        xor_of_num1, xor_of_num2 = 0, 0

        if len2:
            for n in nums1:
                xor_of_num1 ^= n

        if len1:
            for n in nums2:
                xor_of_num2 ^= n

        return xor_of_num1 ^ xor_of_num2


s = Solution()
print(s.xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0]))
print(s.xorAllNums(nums1=[1, 2], nums2=[3, 4]))
