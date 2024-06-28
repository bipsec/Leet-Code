def make_it_white(s):
    lt = 0
    rt = len(s)
    for x in s:
        if x == 'B':
            break
        lt += 1
    for x in s[::-1]:
        if x == 'B':
            break
        rt -= 1
    return rt - lt


def main():
    t = int(input())
    while t > 0:
        n = int(input())
        chars = input()
        res = make_it_white(chars)
        print(res)
        t -= 1


main()
