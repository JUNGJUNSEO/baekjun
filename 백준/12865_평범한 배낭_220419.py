import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0]*(k+1)
for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, -1, -1):
        if i+w <= k:
            dp[i+w] = max(dp[i+w], dp[i]+v)
    print(dp)
