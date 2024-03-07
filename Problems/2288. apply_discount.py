class Solution:

    def discountPrices(self, sentence: str, discount: int) -> str:
        
        sentence = sentence.split()

        res = ""

        for val in sentence:
            if val.startswith("$") and len(val) > 1 and val.count("$") == 1:
                if int(val[1:].isdigit()):
                    price = format(int(val[1:]) - (int(val[1:]) * discount/100), '.2f')
                    res += "$" + str(price)
                else:
                    res += val
            else:
                res += val
            res += " "

        return res.strip()
    
    def discountPrices2(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        result = []

        for word in words:
            if word.startswith("$") and len(word) > 1 and word.count("$") == 1:
                try:
                    price = int(word[1:])
                    if price >= 0:
                        discounted_price = round(price * (1 - discount / 100), 2)
                        result.append(f"${discounted_price:.2f}")
                    else:
                        result.append(word)
                except ValueError:
                    result.append(word)
            else:
                result.append(word)

        return " ".join(result)




s = Solution()
# print(s.discountPrices(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50))
# print(s.discountPrices(sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100))
print(s.discountPrices(sentence = "f32eir5f6hlmmtnlq$zno3zbl5pr26b1xmet6q3rjzs422zqzsezpgi4jqx3h0olb428pk95qndkfz8hereio$2ewx0cnqlvnb6nl$$8iny7t4aemhnqzz6971rnq7pha97e9lf16227j5l2033pnddk $3513024 $516863 $604 $9128265 $945728 $nbf 5az21pm0tj $", 
                       discount = 26))