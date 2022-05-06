import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    k = int(input())
    hmax = list()
    hmin = list()
    d = defaultdict(int)

    for _ in range(k):
        m, n = input().split()
        n = int(n)

        if m == 'I':
            d[n] += 1
            heapq.heappush(hmax, -n)
            heapq.heappush(hmin, n)
        if m == 'D':
            if n == -1:
                while hmin:
                    h = heapq.heappop(hmin)
                    if d[h] != 0:
                        d[h] -= 1
                        break

            else:
                while hmax:
                    h = -heapq.heappop(hmax)
                    if d[h] != 0:
                        d[h] -= 1
                        break
    lst = list()
    for key, val in d.items():
        if val > 0:
            lst.append(key)
    if not lst:
        print('EMPTY')
    else:
        s = sorted(lst, reverse=True)
        print(s[0], s[-1])
