from collections import deque
Inf = int(1e9)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):

    for i in range(n):
        for j in range(m):
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
            if a[nx][ny] != a[x][y]:
                continue

            visit[nx][ny] = True
            q.append((nx, ny))


def get_height():

    min_h = Inf

    for x in range(n):
        for y in range(m):
            if visit[x][y]:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if not in_range(nx, ny):
                        return 0
                    if visit[nx][ny]:
                        continue

                    if a[nx][ny] < a[x][y]:
                        return 0
                    else:
                        min_h = min(min_h, a[nx][ny])

    return min_h


def make_pool(num):

    heigh = get_height()

    if heigh == 0:
        return 0

    cnt = 0

    for i in range(n):
        for j in range(m):
            if visit[i][j]:
                a[i][j] += heigh-num
                cnt += 1

    return cnt * (heigh - num)


def solve(num):
    global ans

    for i in range(n):
        for j in range(m):
            if a[i][j] == num:
                bfs(i, j)
                ans += make_pool(num)


n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
ans = 0

for i in range(1, 10):
    solve(i)

print(ans)
