from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y, color):

    group = list()
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    group.append((x, y))

    while q:

        x, y = q.popleft()

        for i in range(4):

            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue
            if visit[nx][ny] or grid[nx][ny] != color:
                continue

            q.append((nx, ny))
            visit[nx][ny] = True
            group.append((nx, ny))

    return group


def drop():

    for i in range(n):
        for j in range(m):
            next_grid[i][j] = '.'

    for j in range(m):
        last_index = n-1
        for i in range(n-1, -1, -1):

            if grid[i][j] != '.':
                next_grid[last_index][j] = grid[i][j]
                last_index -= 1

    for i in range(n):
        for j in range(m):
            grid[i][j] = next_grid[i][j]


def bomb():

    check = False

    for i in range(n):
        for j in range(m):
            next_grid[i][j] = grid[i][j]
            visit[i][j] = False

    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.' and not visit[i][j]:
                group = bfs(i, j, grid[i][j])
                if len(group) >= 4:
                    check = True
                    for x, y in group:
                        next_grid[x][y] = '.'

    for i in range(n):
        for j in range(m):
            grid[i][j] = next_grid[i][j]

    return check


n, m = 12, 6
grid = [list(input()) for _ in range(n)]
next_grid = [['.'] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]
ans = 0
while True:
    if not bomb():
        break
    drop()

    ans += 1

print(ans)

for i in range(n):
    print(grid[i])
