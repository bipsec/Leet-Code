def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fun():
    n = int(input())
    while n:
        a = int(input())
        print(factorial(a))
        n -= 1


fun()