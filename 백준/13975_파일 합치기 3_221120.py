import sys
from heapq import heappop, heappush
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    k = int(input())
    a = list(map(int, input().split()))
    ans = 0

    q = []
    for i in range(k):
        heappush(q, a[i])

    while len(q) > 1:

        s = heappop(q) + heappop(q)
        ans += s
        heappush(q, s)

    print(ans)
