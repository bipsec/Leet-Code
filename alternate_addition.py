def addition():
    n = int(input())
    num_list = []

    for i in range(n):
        a,b = list(map(int, input().split()))
        num_list.append(a)
        num_list.append(b)
    return num_list


addition()
