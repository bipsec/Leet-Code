import sys

# Personal Header
Iarr = lambda: list(map(int, input().split()))

# Take input array
def takeiar():
    return list(map(int, sys.stdin.readline().rstrip("\r\n").split()))


def solve(arr, length):
    check = 0
    found = False
    for a in range(length - 2):
        for b in range(a + 1, length - 1):
            for c in range(b + 1, length):
                if (arr[a] + arr[b] + arr[c]) % 10 == 3:
                    return "Yes"
    return "No"


def main():
    # Copied from somewhere! :(

    t = int(input())
    while t > 0:
        n = int(input())
        arr = takeiar()
        dict1 = {}
        l = []
        for x in arr:
            y = x % 10
            if y not in dict1:
                dict1[y] = 1
            else:
                if dict1[y] < 3:
                    dict1[y] += 1

        l = []
        for key in dict1:
            h = dict1[key]
            while h != 0:
                l.append(key)
                h -= 1
        print(solve(l, len(l)))

        t = t - 1


if __name__ == '__main__':
    main()

# 6
# 4
# 20 22 19 84
# 4
# 1 11 1 2022
# 4
# 1100 1100 1100 1111
# 5
# 12 34 56 78 90
# 4
# 1 9 8 4
# 6
# 16 38 94 25 18 99
