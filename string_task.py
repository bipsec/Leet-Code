def string_task():
    str1 = list(map(str, input().lower()))

    dupes = ["a", "i", "o", "u", "e", "y"]
    result = ""
    res = "."
    for i in range(len(str1)):
        if str1[i] in dupes:
            str1[i] = ""
    result += "".join(i for i in str1)
    res += ".".join(a for a in result)
    print(res)


string_task()


