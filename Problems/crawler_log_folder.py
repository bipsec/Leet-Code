class Solution:
    def minOperations(self, logs) -> int:
        stack = []

        for item in logs:
            if item == "../":
                if stack:
                    stack.pop()
            elif item == "./":
                continue
            else:
                stack.append(item)

        return len(stack)


s = Solution()
print(s.minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]))
print(s.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
print(s.minOperations(logs=["d1/", "../", "../", "../"]))
print(s.minOperations(logs=["./", "../", "./"]))
