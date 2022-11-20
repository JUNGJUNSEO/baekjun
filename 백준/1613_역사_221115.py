import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
ans = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):

    a, b = map(int, input().split())

    ans[a][b] = -1
    ans[b][a] = 1


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if ans[a][k] == -1 and ans[k][b] == -1:
                ans[a][b] = -1
                ans[b][a] = 1

s = int(input())

for _ in range(s):
    a, b = map(int, input().split())
    print(ans[a][b])

for i in range(1, n + 1):
    print(ans[i][1:])
