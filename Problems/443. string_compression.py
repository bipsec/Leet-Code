class Solution:
    def compress(self, chars):
        
        dupes = {}
        for i in range(len(chars)):
            if chars[i] in dupes:
                dupes[chars[i]] += 1
            else:
                dupes[chars[i]] = 1
        ans = []
        for key, value in dupes.items():
            ans.append(str(key))
            ans.append(str(value))

        return len(ans)


# modify inplace array  -_- -_-


# next to solve - 2696,1750


s  = Solution()
print(s.compress(chars = ["a","a","b","b","c","c","c"]))
print(s.compress(chars = ["a"]))
print(s.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]))