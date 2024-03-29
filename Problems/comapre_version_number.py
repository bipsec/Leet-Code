class Solution:
    def compareVersion(self, version1, version2):
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]

        i, j = 0, 0

        while i < len(versions1) and j < len(versions2):
            if versions1[i] > versions2[j]:
                return 1
            elif versions1[i] < versions2[j]:
                return -1
            i += 1
            j += 1

        while i < len(versions1):
            if versions1[i] > 0:
                return 1
            i += 1

        while j < len(versions2):
            if versions2[j] > 0:
                return -1
            j += 1

        return 0


s = Solution()
print(s.compareVersion(version1="1.01", version2="1.001"))
print(s.compareVersion(version1="1.0", version2="1.1.0"))
print(s.compareVersion(version1="1.0", version2="1.0.1"))
