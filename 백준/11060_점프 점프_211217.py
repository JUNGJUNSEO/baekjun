n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    if not a[i] and not dp[i]:
        print(-1)
        exit()
    for j in range(1, a[i] + 1):
        if i + j < n and not dp[i + j]:
            dp[i + j] = dp[i] + 1
print(dp[-1])
