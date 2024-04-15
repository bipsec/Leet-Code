def matrix():
    t = int(input())
    mat = []
    while t > 0:

        for i in range(0, 8):
            row = list(map(str, input()))
            mat.append(row)
        mat.append("\n")

        t -= 1

    res = ""
    for i in mat:
        for j in range(0, len(i)):
            if i[j] != ".":
                res += i[j]
    print(res)


matrix()
