n = int(input())
a = list(map(int, input().split()))
dp = a.copy()

for i in range(1, n):
    for j in range(i, -1, -1):
        if a[j] < a[i] and a[i] + dp[j] > dp[i]:
            dp[i] = a[i] + dp[j]

print(max(dp))
