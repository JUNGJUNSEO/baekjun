INF = int(1e9)
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
dp = [0] + [INF] * k


for i in range(1, k+1):
    for j in range(n):
        if i-a[j] >= 0:
            dp[i] = min(dp[i], dp[i-a[j]]+1)

print(dp[k] if dp[k] != INF else -1)
