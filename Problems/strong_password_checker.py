# class Solution:
#     def strongPasswordCheckerII(self, password: str) -> bool:
#         seen = set()
#
#         for i, k in enumerate(password):
#             if i > 0 and k == password[i-1]:
#                 return False
#             if k in "!@#$%^&*()-+":
#                 seen.add("S")
#             elif k.isupper():
#                 seen.add("U")
#             elif k.islower():
#                 seen.add("L")
#             elif k.isnumeric():
#                 seen.add("N")
#         if len(seen) == 4 and len(password) > 7:
#             return True
#         return False


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:

        char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
        numeric = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        res = set()
        start, end = 0, len(password)-1

        for i in range(1, len(password)+1):
            while start < end:
                if password[start] == password[start+1]:
                    return False
                start += 1
            if password[i-1] in upper_letters:
                res.add("U")
            elif password[i-1] in lower_letters:
                res.add("L")
            elif password[i-1] in numeric:
                res.add("N")
            elif password[i-1] in char:
                res.add("C")
        # print(res)
        if len(password) > 7 and len(res) == 4:
            return True
        return False



s = Solution()
print(s.strongPasswordCheckerII("IloveLe3tcode!"))
print(s.strongPasswordCheckerII("Me+You-IsMyDream"))
print(s.strongPasswordCheckerII("1aB!"))
print(s.strongPasswordCheckerII("1aaB!"))
print(s.strongPasswordCheckerII("1aBaalkagnowufw!"))
print(s.strongPasswordCheckerII("IloveLec98mjiahwgtcode!"))
print(s.strongPasswordCheckerII("ecuwcfoyajkolntovfniplayrxhzpmhrkhzonopcwxgupzhoupw"))
print(s.strongPasswordCheckerII("XrVIVr-L)CtyZ7xyo!TiHr859lCIHJ$CYHnCQ$kVafJ-15lKjkXLoW5zQnWa3jlGjH9+QKF&^Jvy1$WajBF9VL3^2Okns63LvMZX"))
