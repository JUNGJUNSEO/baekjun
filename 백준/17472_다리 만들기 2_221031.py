from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y, num):

    q = deque()
    q.append((x, y))
    cnt[x][y] = num

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue
            if cnt[nx][ny] >= 0 or not a[nx][ny]:
                continue

            q.append((nx, ny))
            cnt[nx][ny] = num


def make_bridge(ox, oy, num):

    for i in range(4):
        x, y = ox, oy

        while True:

            x, y = x + dx[i], y + dy[i]

            if not in_range(x, y):
                break
            if cnt[x][y] == num:
                break
            if cnt[x][y] >= 0:

                dist = abs(ox-x) + abs(oy-y) - 1

                if dist >= 2:
                    edges.append((dist, num, cnt[x][y]))

                break


def find(x):

    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = [[-1] * m for _ in range(n)]
num = 0


for i in range(n):
    for j in range(m):
        if cnt[i][j] < 0 and a[i][j] == 1:
            bfs(i, j, num)
            num += 1

edges = []
parent = list(range(num))
result = 0

for i in range(n):
    for j in range(m):
        if cnt[i][j] >= 0:
            make_bridge(i, j, cnt[i][j])

edges.sort()

for edge in edges:

    c, a, b = edge

    if find(a) != find(b):
        union(a, b)
        result += c

for i in range(num-1):

    if find(i) != find(i+1):
        print(-1)
        exit()

print(result)
