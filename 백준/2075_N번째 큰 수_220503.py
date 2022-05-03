import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = list()

for i in range(n):
    for x in list(map(int, input().split())):
        if i > 0:
            if x > h[0]:
                heapq.heappop(h)
            else:
                continue
        heapq.heappush(h, x)
print(h[0])
