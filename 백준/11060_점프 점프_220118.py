from collections import deque
n = int(input())
a = list(map(int, input().split()))
dp = [0]*n

q = deque()
q.append(0)
while q:
    x = q.popleft()
    for i in range(1, a[x]+1):
        if x+i < n and not dp[x+i]:
            dp[x+i] = dp[x]+1
            q.append(x+i)
ans = 0
if n > 1:
    if dp[-1]:
        ans = dp[-1]
    else:
        ans = -1

print(ans)
