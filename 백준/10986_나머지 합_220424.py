import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0]*m
s = 0
ans = 0

for i in range(n):
    s += a[i]
    d = s % m

    if d == 0:
        ans += 1

    ans += cnt[d]
    cnt[d] += 1

print(ans)
