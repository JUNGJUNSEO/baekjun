import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
a.sort()
ans = 0
s = a.index(0)
check = False

if (abs(min(a[:s+1])) if a[:s+1] else 0) > (max(a[s+1:]) if a[s+1:] else 0):
    check = True

for i in range(s - (s % m), -1, -m):

    if i == 0 and check:
        ans += abs(a[i])
        break
    ans += abs(a[i]) * 2

for i in range(s + ((n-s) % m), n+1, m):
    if i == n and not check:
        ans += a[i]
        break
    ans += a[i] * 2

print(ans)
