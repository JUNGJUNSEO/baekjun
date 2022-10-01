from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, cnt):
    q.append([x, y])
    path[x][y] = cnt

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] > 0 and path[nx][ny] < 0:
                dfs(nx, ny, cnt+1)


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
path = [[-1]*n for _ in range(n)]


for i in range(n):
    for j in range(n):
        if a[i][j] > 0 and path[i][j] < 0:
            q = deque()
            dfs(i, j, 0)
for i in range(n):
    print(path[i])
