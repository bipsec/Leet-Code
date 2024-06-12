class Solution:
    def complexNumberMultiply(self, num1, num2):
        a, b = num1.split("+")
        c, d = num2.split("+")

        b, d = b[:-1], d[:-1]

        a, b, c, d = map(int, [a, b, c, d])

        real_part = a * c - b * d
        imag_part = a * d + b * c

        return str(real_part) + "+" + str(imag_part) + "i"


s = Solution()
print(s.complexNumberMultiply(num1="1+1i", num2="1+1i"))
print(s.complexNumberMultiply(num1="1+-1i", num2="1+-1i"))
