n = int(input())
a = [int(input()) for _ in range(n)]
dp = [0] * n
for i in range(len(a)):

    if i == 0:
        dp[i] = a[i]
    elif i == 1:
        dp[i] = a[i-1] + a[i]
    elif i == 2:
        dp[i] = max(a[i-2] + a[i], a[i-1] + a[i])
    else:
        dp[i] = max(dp[i-2] + a[i], dp[i-3] + a[i-1] + a[i])

print(dp[n-1])
