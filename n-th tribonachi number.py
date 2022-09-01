class Solution:
    def tribonacci(self, n: int) -> int:

        # dupes = [0, 1, 1, 2]
        #
        # for i in range(4, n+1):
        #     dupes[i % 4] = dupes[(i-1) % 4] + dupes[(i-2) % 4] + dupes[(i-3) % 4]
        # return dupes[n % 4]

        dupes = {0: 0, 1: 1, 2: 1}

        for i in range(3, n + 1):
            dupes[i] = dupes[i - 1] + dupes[i - 2] + dupes[i - 3]

        return dupes[n]





        #### My Approach
        # case1 = [0, 1]
        # dupes = {0: 0, 1: 1}
        #
        # if n == 0:
        #     return list(dupes.keys())[0]
        #
        # for i in range(2, n):
        #     val = case1[i-1] + case1[i-2]
        #     case1.append(val)
        #
        # for i in range(2, len(case1)+1):
        #     if i <= 3:
        #         dupes[i] = sum(dupes.values())
        #     else:
        #         dupes[i] = dupes[i-1] + dupes[i-2] + dupes[i-3]
        #
        # return dupes[len(dupes.keys()) - 1]


s = Solution()
print(s.tribonacci(3))
print(s.tribonacci(0))
print(s.tribonacci(1))
print(s.tribonacci(2))
# print(s.tribonacci(4))
# print(s.tribonacci(5))
print(s.tribonacci(6))
print(s.tribonacci(7))
print(s.tribonacci(25))
