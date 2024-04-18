def lets_check_the_spelling():
    t = int(input())
    name_str = "Timur"
    namer_dictionary = {}

    for item in name_str:
        if item in namer_dictionary:
            namer_dictionary[item] += 1
        else:
            namer_dictionary[item] = 1

    while t > 0:

        num = int(input())
        name = input()

        n = len(namer_dictionary)

        for key, val in namer_dictionary.items():
            if key in name:
                n -= 1
                num -= 1

        if n == 0 and num == 0:
            print("YES")
        else:
            print("NO")

        t -= 1


lets_check_the_spelling()
