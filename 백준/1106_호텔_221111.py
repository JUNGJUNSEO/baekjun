import sys
input = sys.stdin.readline

INF = int(1e9)
c, n = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

dp = [0] + [INF] * 2000

for i in range(1, 2000 + 1):
    for j in range(n):
        if i-a[j][1] >= 0:
            dp[i] = min(dp[i], dp[i-a[j][1]] + a[j][0])

print(min(dp[c:]))
