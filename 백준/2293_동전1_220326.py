from distutils.dir_util import copy_tree
import sys
input = sys.stdin.readline


def solve(c):

    dp[1][c] = 1

    for n in range(c+1, k+1):
        dp[1][n] = dp[1][n-c] + dp[0][n-c]

    for i in range(k+1):
        dp[1][i] += dp[0][i]


n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(2)]

for _ in range(n):

    c = int(input())

    if c > k:
        continue

    solve(c)
    dp[0], dp[1] = dp[1], [0]*(k+1)

print(dp[0][k])
