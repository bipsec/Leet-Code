class Solution:
    def kthSmallestPrimeFraction(self, arr, k: int):
        dupes = {}

        for i in range(len(arr)):
            start, end = i + 1, len(arr)
            while start < end:
                key = str(arr[i]) + "/" + str(arr[start])
                dupes[key] = (arr[i] / arr[start])
                start += 1

        values = sorted(dupes.values())

        for key, val in dupes.items():
            if values[k - 1] == val:
                a, b = key.split("/")
                a = int(a)
                b = int(b)
                return [a, b]


s = Solution()
print(s.kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
print(s.kthSmallestPrimeFraction(arr=[1, 7], k=1))
