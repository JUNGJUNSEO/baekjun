from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
prefix = defaultdict(int)
s = 0
ans = 0

for num in a:
    s += num
    if s == k:
        ans += 1
    if s-k in prefix:
        ans += prefix[s-k]
    prefix[s] += 1

print(ans)
