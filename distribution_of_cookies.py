from heapq import heapify, heappush, heappop

def get_number_mixes(cookies, minimum_value):
    cookies = list(cookies)
    heapify(cookies)
    count = 0
    while cookies[0] < minimum_value:
        if len(cookies) < 2:
            return -1
        heappush(cookies, heappop(cookies) + 2 * heappop(cookies))
        count += 1
        print(cookies)
    return count


# A = [8,15,10,20,8]
# K = 2

A = [6,1,3,2,2,4,1,2]
K = 3
# N, K = map(int, input().split())
# A = map(int, input().split())
print(get_number_mixes(A, K))