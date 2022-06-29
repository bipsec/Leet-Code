class Solution:
    def decodeString(self, s: str) -> str:

        stack = [""]
        num = 0
        it = 0

        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
                # print(num)

            elif s[it] == "[":
                stack.append(num)
                num = 0
                stack.append("")

            elif s[it] == "]":
                st1 = stack.pop()
                res = stack.pop()
                st2 = stack.pop()

                stack.append(st2 + res * st1)

            else:
                stack[-1] += s[it]

            it += 1

        return stack[0]


s = Solution()
print(s.decodeString("3[a]2[bc]2[a]"))
print(s.decodeString("3[a5[c]]4[b]"))
