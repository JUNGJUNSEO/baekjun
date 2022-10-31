from heapq import heappop, heappush
import sys
input = sys.stdin.readline

h1 = []
h2 = []

n = int(input())

for _ in range(n):

    x = int(input())
    l1, l2 = len(h1), len(h2)

    if l1 == l2:

        if not h2:
            heappush(h1, -x)
        else:
            if h2[0] < x:
                heappush(h1, heappop(h2))
                heappush(h2, x)
            else:
                heappush(h1, -x)

    elif l1 > l2:

        if -h1[0] > x:
            heappush(h2, -heappop(h1))
            heappush(h1, -x)
        else:
            heappush(h2, x)

    print(-h1[0])
