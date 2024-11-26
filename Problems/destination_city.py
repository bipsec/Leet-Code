class Solution:
    def destCity(self, paths) -> str:
        dupes = {}

        for a, b in paths:
            dupes[a] = b

        stack = [paths[0][0]]

        while True:
            modified = False
            for key, val in dupes.items():
                if stack and key == stack[-1]:
                    stack.pop()
                    stack.append(val)
                    modified = True
                    break
            if not modified:
                break

        return stack[0]


s = Solution()
# print(s.destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))
print(s.destCity(paths=[["B", "C"], ["A", "Z"], ["C", "A"]]))
print(s.destCity(paths=[["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],["TtnllZpKKg","OAxMijOZgW"]]))
# print(s.destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
# print(s.destCity(paths=[["London", "New York"]]))
