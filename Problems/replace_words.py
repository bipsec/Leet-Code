class Solution:
    def replaceWords(self, dictionary, sentence):
        pass

    def maximumProduct(self, nums) -> int:
        nums.sort()
        maxProd = 1
        res = 1
        if len(nums) > 3:
            for i in range(2, len(nums)):
                res = nums[i - 2] * nums[i - 1] * nums[i]
                if maxProd < res:
                    maxProd = res
        else:
            for i in range(len(nums)):
                res *= nums[i]
            return res

        return maxProd

    def maximumCount(self, nums) -> int:
        start, end = 0, len(nums) -1
        c = 0
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < 0:
                mid += 1
            elif nums[mid] == 0:
                c += 1

        negCount = mid
        posCount = len(nums) - negCount - c

        print(negCount, posCount)




s = Solution()
# print(s.replaceWords(dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery"))
# print(s.replaceWords(dictionary=["a", "b", "c"], sentence="aadsfasf absbs bbab cadsfafs"))
# print(s.maximumProduct(nums=[1, 2, 3]))
# print(s.maximumProduct(nums=[1, 2, 3, 4]))
# print(s.maximumProduct(nums=[-1, -2, -3]))
# print(s.maximumProduct(nums=[1, 3, 2, 6, 2, 1]))
print(s.maximumCount(nums=[-100, -98, -1, 2, 3, 4]))
print(s.maximumCount(nums=[-2, -1, -1, 1, 2, 3]))
print(s.maximumCount(nums=[5, 20, 66, 1314]))
print(s.maximumCount(nums=[-3, -2, -1, 0, 0, 1, 2]))
print(s.maximumCount(nums=[-1563, -236, -114, -55, 427, 447, 687, 752, 1021, 1636]))


