from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def bfs(x, y, num):

    q = deque()
    q.append((x, y))
    cluster[x][y] = num

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if grid[nx][ny] == '.' or cluster[nx][ny] >= 0:
                continue

            q.append((nx, ny))
            cluster[nx][ny] = num


def find_cluster():

    for i in range(r):
        for j in range(c):
            cluster[i][j] = -1

    # 바닥에 붙어 있는 cluster
    for j in range(c):

        if grid[r-1][j] == '.' or cluster[r-1][j] >= 0:
            continue

        bfs(r-1, j, 0)

    # 공중에 떠있는 cluster
    for i in range(r-1):
        for j in range(c):

            if grid[i][j] == '.' or cluster[i][j] >= 0:
                continue

            bfs(i, j, 1)


def get_distance():

    dist = r

    for i in range(r):
        for j in range(c):
            if cluster[i][j] == 1:
                d = 0
                for _ in range(r-i-1):

                    d += 1

                    if cluster[i+d][j] == 0:
                        d -= 1
                        break

                dist = min(dist, d)

    return dist


def drop_cluster():

    for i in range(r):
        for j in range(c):
            next_grid[i][j] = '.'

    dist = get_distance()

    for i in range(r):
        for j in range(c):
            if cluster[i][j] == 1:
                next_grid[i+dist][j] = grid[i][j]

            elif cluster[i][j] == 0:
                next_grid[i][j] = grid[i][j]

    for i in range(r):
        for j in range(c):
            grid[i][j] = next_grid[i][j]


r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
next_grid = [['.'] * c for _ in range(r)]
cluster = [[False] * c for _ in range(r)]
n = int(input())
a = list(map(int, input().split()))


for i in range(n):

    if i % 2 == 0:
        for j in range(c):
            if grid[r-a[i]][j] == 'x':

                grid[r-a[i]][j] = '.'
                break
    else:
        for j in range(c-1, -1, -1):
            if grid[r-a[i]][j] == 'x':
                grid[r-a[i]][j] = '.'
                break

    find_cluster()
    drop_cluster()

for i in range(r):
    print(''.join(grid[i]))
