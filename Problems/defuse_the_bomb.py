class Solution:
    def decrypt(self, code, k: int):

        output = []
        for i in range(len(code)):
            if k > 0:
                sum = 0
                j = i + 1
                m = k
                while (m):
                    sum += code[j % len(code)]
                    m -= 1
                    j += 1
                output.append(sum)

            elif k == 0:
                output.append(0)

            else:
                sum = 0
                j = i - 1
                m = k
                while (m):
                    sum += code[j % len(code)]
                    m += 1
                    j -= 1
                output.append(sum)

        return output

# not mine


s = Solution()
print(s.decrypt(code=[5, 7, 1, 4], k=3))
print(s.decrypt(code=[1, 2, 3, 4], k=0))
print(s.decrypt(code=[2, 4, 9, 3], k=-2))
print(s.decrypt(code=[5, 2, 2, 3, 1], k=3))
