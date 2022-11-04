from collections import deque

dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, 1, 1, -1, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def get_distance():

    dist = n * m

    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                dist = min(dist, cnt[i][j])

    return dist


def bfs(x, y):

    for i in range(n):
        for j in range(m):
            cnt[i][j] = -1

    q = deque()
    q.append((x, y))
    cnt[x][y] = 0

    while q:

        x, y = q.popleft()

        for i in range(8):

            nx, ny = x + dx[i], y + dy[i]
            if not in_range(nx, ny):
                continue
            if cnt[nx][ny] >= 0:
                continue

            q.append((nx, ny))
            cnt[nx][ny] = cnt[x][y] + 1


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = [[-1] * m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            bfs(i, j)
            ans = max(get_distance(), ans)

print(ans)
