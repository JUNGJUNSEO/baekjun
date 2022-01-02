n = int(input())
a = list(map(int, input().split()))
dp = [0]*n
for i in range(n-1):
    for j in range(1, a[i]+1):
        dp[i+j] = min(dp[i+j], dp[i+1]+1)
print(dp)
