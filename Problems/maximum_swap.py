class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last = {int(d): i for i, d in enumerate(num_str)}

        for i, d in enumerate(num_str):
            for x in range(9, int(d), -1):
                if last.get(x, -1) > i:
                    # Perform the swap
                    num_str[i], num_str[last[x]] = num_str[last[x]], num_str[i]
                    return int(''.join(num_str))

        return num


s = Solution()
print(s.maximumSwap(num=2736))
print(s.maximumSwap(num=9973))
