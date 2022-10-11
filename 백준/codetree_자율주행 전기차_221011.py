from collections import deque
Inf = int(1e9)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(n):
        for j in range(n):
            dist[i][j] = -1

    q = deque()
    q.append((x, y))
    dist[x][y] = 0

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not in_range(nx, ny):
                continue
            if dist[nx][ny] >= 0 or load[nx][ny] == 1:
                continue

            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1


def find_passenger():

    s = (Inf, n, n)
    num = -1

    for idx, (sx, sy, _, _) in enumerate(passengers):

        if arrived[idx]:
            continue
        if dist[sx][sy] < 0:
            continue

        d = dist[sx][sy]

        if s > (d, sx, sy):
            s = (d, sx, sy)
            num = idx

    return num


n, m, c = map(int, input().split())
load = [list(map(int, input().split())) for _ in range(n)]
ax, ay = map(int, input().split())
ax, ay = ax-1, ay-1
dist = [[-1]*n for _ in range(n)]
arrived = [False]*m
passengers = []

for i in range(m):
    sx, sy, ex, ey = map(int, input().split())
    sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1
    passengers.append((sx, sy, ex, ey))

for _ in range(m):
    bfs(ax, ay)
    num = find_passenger()
    if num < 0:
        print(-1)
        exit()
    sx, sy, ex, ey = passengers[num]
    d = dist[sx][sy]
    c -= d
    bfs(sx, sy)
    d = dist[ex][ey]
    if d < 0:
        print(-1)
        exit()
    c -= d
    if c < 0:
        print(-1)
        exit()
    c += 2*d
    arrived[num] = True
    ax, ay = ex, ey

print(c)

# 1.
# passenger의 도착위치 또는 시작 위치가 같을 수도 있음.
# 따라서 도착 위치, 시작 위치를 2차원 배열에 그냥 표시하는 것 보다는
# 1 차원 배열에 담는 것이 코드 구현에 훨씬 좋음.
# ex. 1번 승객일 경우
# passengers 배열에
# passengers[1] = [시작_x, 시작_y, 끝_x, 끝_y]
