import sys
from itertools import combinations
input = sys.stdin.readline


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize

for i in range(1, n+1):
    for case in combinations(a, i):
        mul, sum = 1, 0
        for s, b in case:
            mul *= s
            sum += b
        ans = min(ans, abs(mul-sum))

print(ans)
