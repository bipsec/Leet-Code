def comparison():
    n = int(input())
    s = input()
    cnt = 0
    temp = 0
    i = 0

    while i < n:
        temp = 1
        while i < n and s[i] == '<':
            temp += 1
            i += 1
        if cnt < temp:
            cnt = temp
        temp = 1
        while i < n and s[i] == '>':
            temp += 1
            i += 1
        if cnt < temp:
            cnt = temp

    print(cnt)


if __name__ == '__main__':
    t = int(input())

    while t > 0:
        comparison()
        t -= 1
