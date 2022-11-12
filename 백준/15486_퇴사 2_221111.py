import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n+1):
    t, p = map(int, input().split())

    if i+t-1 <= n:
        dp[i+t-1] = max(dp[i+t-1], max(dp[:i]) + p)


print(max(dp))
