n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n-1)
for i in range(n):
    for j in range(1, a[i] + 1):
        if i + j < n and not dp[i + j]:
            dp[i + j] = dp[i] + 1
if n == 1:
    print(0)
else:
    print(a[-1])