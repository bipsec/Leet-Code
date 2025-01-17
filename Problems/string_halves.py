class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowels = "aeiouAEIOU"

        first_half = s[:len(s) // 2]
        second_half = s[len(s) // 2:]

        vowel_counter = 0
        consonant_counter = 0

        for item in range(len(s) // 2):
            if first_half[item] in vowels:
                vowel_counter += 1
            if second_half[item] in vowels:
                vowel_counter -= 1
            if first_half[item] not in vowels:
                consonant_counter += 1
            if second_half[item] not in vowels:
                consonant_counter -= 1

        # print(vowel_counter, "---", consonant_counter)
        return vowel_counter == consonant_counter


s = Solution()
print(s.halvesAreAlike(s="textbook"))
print(s.halvesAreAlike(s="book"))
print(s.halvesAreAlike(s="fuck"))
print(s.halvesAreAlike(s="ogenkidesukahaigenkidesu"))
print(s.halvesAreAlike(s="ogenkidesukahaigenkidesu"))
print(s.halvesAreAlike(s="OMEDETOUGOZAIMASU"))
