class Solution:
    def commonChars(self, words):
        if not words:
            return []

        dupes = [{} for _ in words]

        for i, string in enumerate(words):
            for char in string:
                if char in dupes[i]:
                    dupes[i][char] += 1
                else:
                    dupes[i][char] = 1

        min_freq = {}

        for char_dict in dupes:
            for char, freq in char_dict.items():
                if char in min_freq:
                    min_freq[char] = min(min_freq[char], freq)
                else:
                    min_freq[char] = freq

        common_chars = []
        for char, freq in min_freq.items():
            if all(char in char_dict for char_dict in dupes):
                common_chars.extend([char] * freq)

        return common_chars


s = Solution()
print(s.commonChars(words=["bella", "label", "roller"]))
print(s.commonChars(words=["cool", "lock", "cook"]))
