#  Codecheff

def best_of_two():
    n = int(input())

    for i in range(0, n):

        a = list(map(int, input().strip().split()))

        if a[0] >= a[1]:
            print(a[0])
        elif a[0] <= a[1]:
            print(a[1])


best_of_two()