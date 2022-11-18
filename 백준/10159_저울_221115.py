import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

ans = [[-1] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    ans[a][b] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if ans[a][k] == 0 and ans[k][b] == 0:
                ans[a][b] = 0

res = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if ans[i][j] == 0:
            res[i] += 1
            res[j] += 1

for i in range(1, n + 1):
    print(n - res[i] - 1)
