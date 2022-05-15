from collections import deque
import sys
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(z, x, y, h):
    q = deque()
    q.append((x, y, z, h, 0))
    move[z][x][y] = 0

    while q:
        x, y, z, h, d = q.popleft()
        if a[x][y] == 'E':
            break
        if h == 0:
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if move[z][nx][ny] < 0:
                    if a[nx][ny] == 'U':
                        a[nx][ny] = '.'
                        q.append((nx, ny, z+1, h, u-1))
                        move[z+1][nx][ny] = move[z][x][y] + 1
                    else:
                        if d > 0:
                            q.append((nx, ny, z, h, d-1))
                        elif d == 0:
                            q.append((nx, ny, z, h-1, d))
                        move[z][nx][ny] = move[z][x][y] + 1


n, h, u = map(int, input().split())
a = [list(input()) for _ in range(n)]
k = 10

for i in range(n):
    for j in range(n):
        if a[i][j] == 'S':
            a[i][j] == '.'
            sx, sy = i, j
        if a[i][j] == 'E':
            ex, ey = i, j

move = [[[-1]*n for _ in range(n)] for _ in range(k+1)]
bfs(0, sx, sy, h)

ans = sys.maxsize

for i in range(k+1):
    if move[i][ex][ey] > 0:
        ans = min(ans, move[i][ex][ey])

print(ans if ans != sys.maxsize else -1)

for i in range(n):
    print(a[i])
