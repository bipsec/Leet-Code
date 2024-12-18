class Solution:

    def check_prime(self, n):

        if n <= 1:
            return False

        for i in range(2, int(n ** 0.5) + 1):

            if n % i == 0:
                return False

        return True

    def maximumPrimeDifference(self, nums):

        dupes = []
        for item in range(len(nums)):
            prime = self.check_prime(nums[item])

            if prime:
                dupes.append(item)

        if len(dupes) > 1:
            return dupes[-1] - dupes[0]
        else:
            return 0


s = Solution()
print(s.maximumPrimeDifference(nums=[4, 2, 9, 5, 3]))
print(s.maximumPrimeDifference(nums=[4, 8, 2, 8]))
print(s.maximumPrimeDifference(nums=[4, 8, 2, 8]))
