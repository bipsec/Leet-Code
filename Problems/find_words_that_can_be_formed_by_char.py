class Solution:

    def check(self, word, check_dict):

        for j in range(len(word)):
            if word[j] in check_dict.keys():
                if check_dict[word[j]] >= 1:
                    check_dict[word[j]] -= 1
            else:
                return True

    def countCharacters(self, words, chars: str) -> int:

        dupes = {}

        for i in range(len(chars)):
            if chars[i] not in dupes:
                dupes[chars[i]] = 1
            else:
                dupes[chars[i]] += 1
        res = 0

        for item in words:
            check = self.check(item, dupes)
            if not check:
                res += len(item)
        return res


s = Solution()
print(s.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))
print(s.countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"))
print(s.countCharacters(
    words=["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
           "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb", "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl", "boygirdlggnh",
           "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
           "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
           "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
           "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr", "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
           "oxgaskztzroxuntiwlfyufddl",
           "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
           "qnagrpfzlyrouolqquytwnwnsqnmuzphne", "eeilfdaookieawrrbvtnqfzcricvhpiv",
           "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz", "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
           "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
           "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo",
           "teyygdmmyadppuopvqdodaczob", "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
           "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"],
    chars="usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"))
