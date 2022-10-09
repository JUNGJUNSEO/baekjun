from collections import deque


def bfs(ox, oy):
    global ans
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visit = [[False]*m for _ in range(n)]
    visit[ox][oy] = True
    q = deque()
    q.append((ox, oy))
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if visit[nx][ny] or a[nx][ny] != a[ox][oy]:
                continue

            visit[nx][ny] = True
            q.append((nx, ny))
            cnt += 1

    ans += cnt*a[ox][oy]


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
dx, dy = 0, 1
ans = 0
dice = [1, 3, 5, 2, 4, 6]

up, right, front = 0, 1, 2


x, y = x+dx, y+dy
bfs(x, y)
# 동쪽으로
up, right, front = 5-right, up, front

for _ in range(k-1):

    bottom = 5-up

    if dice[bottom] > a[x][y]:
        dx, dy = dy, -dx
    elif dice[bottom] < a[x][y]:
        dx, dy = -dy, dx
    else:
        dx, dy = dx, dy

    x, y = x+dx, y+dy

    if not (0 <= x < n and 0 <= y < m):
        dx, dy = -dx, -dy
        x, y = x+2*dx, y+2*dy

    bfs(x, y)

    # 동쪽으로
    if dx == 0 and dy == 1:
        up, right, front = 5-right, up, front
    # 서쪽으로
    elif dx == 0 and dy == -1:
        up, right, front = right, 5-up, front
    # 남쪽으로
    elif dx == 1 and dy == 0:
        up, right, front = 5-front, right, up
    # 북쪽으로
    elif dx == -1 and dy == 0:
        up, right, front = front, right, 5-up

print(ans)
