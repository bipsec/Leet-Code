class Solution:
    def find_divisors_optimized(self, n: int):
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        divisors.sort()
        return divisors

    def closestDivisors(self, num: int):
        new_Num = num + 1
        new_Num2 = new_Num + 1

        get_Num_divisors = self.find_divisors_optimized(new_Num)
        get_Num2_divisors = self.find_divisors_optimized(new_Num2)

        closest_pair = None
        min_diff = float('inf')

        for i in range(len(get_Num_divisors)):
            x = get_Num_divisors[i]
            y = new_Num // x
            if abs(x - y) < min_diff:
                closest_pair = [x, y]
                min_diff = abs(x - y)

        for i in range(len(get_Num2_divisors)):
            a = get_Num2_divisors[i]
            b = new_Num2 // a
            if abs(a - b) < min_diff:
                closest_pair = [a, b]
                min_diff = abs(a - b)

        return closest_pair


s = Solution()
print(s.closestDivisors(8))
print(s.closestDivisors(123))
print(s.closestDivisors(999))
