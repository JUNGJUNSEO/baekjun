from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
prefix = defaultdict(int)
s = 0
ans = 0

for i in range(n):
    s += a[i]
    d = s % m

    if d == 0:
        ans += 1
    if d in prefix:
        ans += prefix[d]

    prefix[d] += 1

print(ans)
