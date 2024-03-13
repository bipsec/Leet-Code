import math
from itertools import compress

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

#this one is pretty worthy for getting prime numbers in a range

def primes(n):
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]


primes(4)

# //two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000)
