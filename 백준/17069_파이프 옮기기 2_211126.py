import sys
input = sys.stdin.readline


def go(x, y, pipe):
    if x == n-1 and y == n-1:
        return 1
    if dp[x][y]:
        return dp[x][y]
    if pipe == 0 or pipe == 2:
        if y+1 < n and not a[x][y+1]:
            dp[x][y] += go(x, y+1, 0)
    if pipe == 1 or pipe == 2:
        if x+1 < n and not a[x+1][y]:
            dp[x][y] += go(x+1, y, 1)
    if pipe == 0 or pipe == 1 or pipe == 2:
        if x+1 < n and y+1 < n and not a[x][y+1] and not a[x+1][y] and not a[x+1][y+1]:
            dp[x][y] += go(x+1, y+1, 2)
    return dp[x][y]


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
print(go(0, 1, 0))
