def find():
    string1 = list(map(str, input().lower()))
    string2 = list(map(str, input().lower()))

    if string1 == string2:
        res = 0
    elif string1 > string2:
        res = 1
    elif string1 < string2:
        res = -1
    print(res)


find()
