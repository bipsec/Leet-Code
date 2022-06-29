class Solution:

    def SieveOfEratosthenes(self, n):

        prime = [True for i in range(n+1)]
        p = 2
        count = 0

        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1

        for i in range(2, n+1):
            if prime[i]:
                count += 1
        return count


s = Solution()
print(s.SieveOfEratosthenes(10))
# print(s.SieveOfEratosthenes(20))
# SieveOfEratosthenes(10)
