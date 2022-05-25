import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a += a
left, right = 0, 0
ans = 0
length = len(a)
d = defaultdict(int)

while right < length:

    if right-left < k:
        d[a[right]] += 1
        right += 1
    else:
        if c not in d:
            ans = max(ans, len(d)+1)
        else:
            ans = max(ans, len(d))
        d[a[left]] -= 1
        if d[a[left]] == 0:
            del d[a[left]]
        left += 1

print(ans)
