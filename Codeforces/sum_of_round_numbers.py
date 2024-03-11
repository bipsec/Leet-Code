def make_round(number):
    if number < 10:
        return [number]
    else:
        digits = list(str(number))
        rounded_parts = []
        for i, digit in enumerate(digits):
            rounded_digit = int(digit) * 10 ** (len(digits) - 1 - i)
            if rounded_digit != 0:
                rounded_parts.append(rounded_digit)
        return rounded_parts


def sum_of_rounds():
    t = int(input())
    nums = []
    for i in range(t):
        val = int(input())
        nums.append(val)
    
    for i in nums:
        getValues = make_round(i)
        getTotal = len(getValues)
        print(getTotal)
        print(" ".join(str(i) for i in getValues))
        

sum_of_rounds()

