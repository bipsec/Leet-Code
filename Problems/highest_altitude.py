class Solution:
    def largestAltitude(self, gain) -> int:
        ans = 0
        arr = [0]
        for i in range(len(gain)):
            ans += gain[i]
            arr.append(ans)
        return max(arr)


# mine

s = Solution()
print(s.largestAltitude([-5, 1, 5, 0, -7]))
print(s.largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]))
