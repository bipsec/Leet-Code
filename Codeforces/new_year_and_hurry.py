def new_year_and_hurry():
    a, b = map(int, input().split())
    res = 240 - b
    output = 0
    c = 0

    for i in range(1, a + 1):
        output += 5 * i
        if output > res:
            break
        else:
            c += 1

    print(c)


new_year_and_hurry()
