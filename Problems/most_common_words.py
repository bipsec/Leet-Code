import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        paragraph = paragraph.lower()
        symbols = ["!", "?", "'", ",", ";", ".", " "]
        split_pattern = f"[{''.join(map(re.escape, symbols))}]"
        split_text = re.split(split_pattern, paragraph)
        split_text = [s for s in split_text if s]

        # print(split_text)

        dupes = {}
        for char in split_text:
            if char not in dupes:
                dupes[char] = 1
            else:
                dupes[char] += 1

        if len(banned) >= 1:
            for item in banned:
                if item in dupes.keys():
                    dupes.pop(item)

        maxVal = max(dupes.values())

        for key, val in dupes.items():
            if maxVal == val:
                return key



s = Solution()
print(s.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]))
print(s.mostCommonWord(paragraph="a.", banned=[]))
print(s.mostCommonWord("a. b. a.a", ["b"]))
print(s.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
print(s.mostCommonWord("abc abc? abcd the jeff!", ["abc", "abcd", "jeff"]))  # Output: the
