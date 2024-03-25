class Solution:
    def compress(self, chars) -> int:
        if len(chars) <= 1:
            return len(chars)

        compressed_index = 0
        current_char = chars[0]
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == current_char:
                count += 1
            else:
                chars[compressed_index] = current_char
                compressed_index += 1
                if count > 1:
                    for digit in str(count):
                        chars[compressed_index] = digit
                        compressed_index += 1
                current_char = chars[i]
                count = 1

        chars[compressed_index] = current_char
        compressed_index += 1
        if count > 1:
            for digit in str(count):
                chars[compressed_index] = digit
                compressed_index += 1

        return compressed_index


# not mine


s = Solution()
print(s.compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
print(s.compress(chars=["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "a", "c"]))
print(s.compress(chars=["a", "b", "c", "d", "a", "v", "c"]))
print(s.compress(chars=["a"]))
