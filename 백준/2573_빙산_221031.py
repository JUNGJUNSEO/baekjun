from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def melt():

    for i in range(n):
        for j in range(m):
            next_grid[i][j] = 0

    for x in range(n):
        for y in range(m):
            if grid[x][y]:

                cnt = 0

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if not grid[nx][ny]:
                        cnt += 1

                res = grid[x][y] - cnt
                next_grid[x][y] = res if res >= 0 else 0

    for i in range(n):
        for j in range(m):
            grid[i][j] = next_grid[i][j]


def bfs(x, y):

    q = deque()
    q.append((x, y))
    visit[x][y] = True

    while q:

        x, y = q.popleft()

        for i in range(4):

            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue
            if visit[nx][ny] or grid[nx][ny] == 0:
                continue

            q.append((nx, ny))
            visit[nx][ny] = True


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]
ans = 0

while True:

    ans += 1

    for i in range(n):
        for j in range(m):
            visit[i][j] = False

    melt()

    cnt = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visit[i][j]:
                cnt += 1
                bfs(i, j)

    if cnt >= 2:
        print(ans)
        break

    elif cnt == 0:
        print(0)
        break
