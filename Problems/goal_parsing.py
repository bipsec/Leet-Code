class Solution:
    def interpret(self, command: str) -> str:
        left, right = 0, len(command) - 1
        stack = []
        ans = ""

        while left <= right:
            if command[left] == "G":
                ans += "G"
            else:
                if command[left] == "(" and command[left+1] == ")":
                    ans += "o"
                elif command[left] == "(" and command[left+1] == "a":
                    ans += "al"
            left += 1
        return ans


s = Solution()
print(s.interpret(command="G()(al)"))
print(s.interpret(command="(al)G(al)()()G"))
print(s.interpret(command="G()()()()(al)"))
