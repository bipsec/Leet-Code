class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:

        d = {}
        dupes = []
        for i in range(len(s)):
            d[indices[i]] = s[i]
        for key, value in sorted(d.items()):
            dupes.append(value)

        return "".join(dupes)

        # res = [""] * len(s)
        # for key, value in enumerate(s):
        #     res[indices[key]] = value
        # return "".join(res)


s = Solution()
print(s.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
print(s.restoreString("abc", [0, 1, 2]))

