from collections import deque
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(lst):
    q = deque()
    for x, y, z in lst:
        q.append((x, y, z))
        day[z][x][y] = 0

    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if box[nz][nx][ny] == 0 and day[nz][nx][ny] < 0:
                    q.append((nx, ny, nz))
                    day[nz][nx][ny] = day[z][x][y] + 1


m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
day = [[[-1]*m for _ in range(n)] for _ in range(h)]
mellow = list()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if box[k][i][j] == 1:
                mellow.append((i, j, k))
            if box[k][i][j] == -1:
                day[k][i][j] = 0
bfs(mellow)

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(h):
            if day[k][i][j] == -1:
                print(-1)
                exit()
            ans = max(ans, day[k][i][j])
print(ans)
