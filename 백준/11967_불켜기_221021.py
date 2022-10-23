from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def turn_on(x, y):

    if not remote[x][y]:
        return

    while remote[x][y]:
        nx, ny = remote[x][y].pop()
        light[nx][ny] = 1

    return True


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(x, y):

    for i in range(n):
        for j in range(n):
            visit[i][j] = False

    visit[x][y] = True
    q = deque()
    q.append((x, y))

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue
            if visit[nx][ny]:
                continue
            if not light[nx][ny]:
                continue

            q.append((nx, ny))
            visit[nx][ny] = True
            turn_on(nx, ny)


n, m = map(int, input().split())
x, y = 0, 0
light = [[0]*n for _ in range(n)]
visit = [[False]*n for _ in range(n)]
remote = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    remote[x1-1][y1-1].append((x2-1, y2-1))

light[x][y] = 1
turn_on(x, y)

ans = 0

while True:
    bfs(x, y)
    temp = sum(sum(light[i]) for i in range(n))

    if temp > ans:
        ans = temp
    else:
        break

print(ans)
