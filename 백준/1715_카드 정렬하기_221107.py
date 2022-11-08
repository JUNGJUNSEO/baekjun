from heapq import heappop, heappush

n = int(input())
q = []
for _ in range(n):
    heappush(q, int(input()))

ans = 0

while len(q) > 1:

    s = heappop(q) + heappop(q)
    ans += s
    heappush(q, s)

print(ans)
