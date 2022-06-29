class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        case1 = case2 = 1
    

        for i in range(2, n):
            result = case1 + case2
            case1 = case2
            case2 = result
        return result


s = Solution()
print(s.fib(4))
