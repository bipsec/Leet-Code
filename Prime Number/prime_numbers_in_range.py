import math


def isPrime(n):
    limit = math.floor(math.sqrt(n))
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_in_range():
    t = int(input())
    for _ in range(t):
        lower, upper = (map(int, input().split()))

        for i in range(lower, upper + 1):
            if isPrime(i):
                print(i)
        print()


primes_in_range()


//two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000)
