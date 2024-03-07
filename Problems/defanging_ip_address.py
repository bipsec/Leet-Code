class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""

        for i in range(len(address)):
            if address[i] == ".":
                result += "[.]"
            else:
                result += address[i]

        return result


s = Solution()
print(s.defangIPaddr(address="1.1.1.1"))
print(s.defangIPaddr(address="255.100.50.0"))
