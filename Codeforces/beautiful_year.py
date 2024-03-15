def beautiful_year():
    get_input = int(input())
    for i in range(get_input, 10000, 1):
        res = i + 1
        if len(set(str(res))) == len(str(res)):
            return res


print(beautiful_year())
