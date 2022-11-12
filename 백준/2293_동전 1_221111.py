import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
dp = [1] + [0] * k

for i in range(n):
    for j in range(1, k+1):
        if j-a[i] >= 0:
            dp[j] += dp[j-a[i]]

print(dp[k])
