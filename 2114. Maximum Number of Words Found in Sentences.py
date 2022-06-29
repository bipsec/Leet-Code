class Solution:
    def mostWordsFound(self, sentences):
        return max((len(sentence.split())) for sentence in sentences)





s = Solution()
print(s.mostWordsFound(["w jrpihe zsyqn l dxchifbxlasaehj",
                        "nmmfrwyl jscqyxk a xfibiooix xolyqfdspkliyejsnksfewbjom",
                        "xnleojowaxwpyogyrayfgyuzhgtdzrsyococuqexggigtberizdzlyrdsfvryiynhg",
                        "krpwiazoulcixkkeyogizvicdkbrsiiuhizhkxdpssynfzuigvcbovm",
                        "rgmz rgztiup wqnvbucfqcyjivvoeedyxvjsmtqwpqpxmzdupfyfeewxegrlbjtsjkusyektigr",
                        "o lgsbechr lqcgfiat pkqdutzrq iveyv iqzgvyddyoqqmqerbmkxlbtmdtkinlk",
                        "hrvh efqvjilibdqxjlpmanmogiossjyxepotezo",
                        "qstd zui nbbohtuk",
                        "qsdrerdzjvhxjqchvuewevyzlkyydpeeblpc"])
      )
