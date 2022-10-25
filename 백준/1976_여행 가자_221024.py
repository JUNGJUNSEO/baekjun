import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):

    visit[y] = True
    check[x][y] = True

    for ny in graph[y]:
        if not visit[ny]:
            dfs(x, ny)


n = int(input())
m = int(input())
check = [[False] * n for _ in range(n)]
graph = [[] for _ in range(n)]

for x in range(n):
    for y, num in enumerate(list(map(int, input().split()))):
        if num == 1:
            graph[x].append(y)

for i in range(n):

    visit = [False]*n

    dfs(i, i)

p = list(map(int, input().split()))
ans = 'YES'

for i in range(m - 1):
    c1, c2 = p[i:i+2]

    if not check[c1-1][c2-1]:
        ans = 'NO'
        break

print(ans)
