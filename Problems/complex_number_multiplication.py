class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return "{}{:+}i".format(self.real, self.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)


class Solution:
    def complexNumberMultiply(self, num1, num2):
        a, b = num1.split("+")
        c, d = num2.split("+")

        nums = ComplexNumber(int(a), int(b[:-1]))
        nums2 = ComplexNumber(int(c), int(d[:-1]))

        ans = nums * nums2

        if str("-") in str(ans):
            return f"{ans.real}+{ans.imag}i"
        else:
            return str(ans)


s = Solution()
print(s.complexNumberMultiply(num1="1+1i", num2="1+1i"))
print(s.complexNumberMultiply(num1="1+-1i", num2="1+-1i"))
