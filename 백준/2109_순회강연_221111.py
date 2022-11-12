from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x: x[1])

q = []


for i in range(n):

    heappush(q, a[i][0])

    if len(q) > a[i][1]:
        heappop(q)


print(sum(q))
