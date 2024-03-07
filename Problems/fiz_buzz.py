class Solution:
    def fizzBuzz(self, n: int):

        arr = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                st = "FizzBuzz"
                arr.append(st)
            elif i % 5 == 0:
                st = "Buzz"
                arr.append(st)
            elif i % 3 == 0:
                st = "Fizz"
                arr.append(st)
            else:
                arr.append(str(i))
        return arr


s = Solution()
print(s.fizzBuzz(3))
