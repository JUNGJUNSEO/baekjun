from collections import deque

# 왼쪽, 위, 오른쪽, 아래
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def air_con(x, y, d):
    # 에어컨 바로 앞에 벽이 있을 경우.
    if w[x][y][d]:
        return

    air = [[0]*n for _ in range(n)]
    nx, ny = x+dx[d], y+dy[d]
    air[nx][ny] = 5
    q = deque()
    q.append((nx, ny, 5))

    while q:
        x, y, c = q.popleft()

        # 차가운 공기가 없는 경우.
        if not c:
            break

        paths = [[(d-1+4) % 4, d], [(d+1) % 4, d], [d]]
        for path in paths:
            sx, sy = x, y
            can_go = True
            for i in path:
                ox, oy = sx, sy
                sx, sy = sx+dx[i], sy+dy[i]
                # 범위를 벗어난 경우 or 벽이 있는 경우.
                if not (0 <= sx < n and 0 <= sy < n) or w[ox][oy][i]:
                    can_go = False
                    break

            # 공간에 갈 수 있고 차가운 공기가 들어 있지 않은 경우.
            if can_go and not air[sx][sy]:
                air[sx][sy] = c-1
                q.append((sx, sy, c-1))

    return air


def air_mix():

    temp = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp[i][j] = t[i][j]

    for x in range(n):
        for y in range(n):
            for i in range(4):
                # 벽이 있을 경우.
                if w[x][y][i]:
                    continue
                nx, ny = x+dx[i], y+dy[i]
                # 범위를 벗어날 경우.
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if t[x][y] > t[nx][ny]:
                    temp[x][y] -= (t[x][y] - t[nx][ny]) // 4
                else:
                    temp[x][y] += (t[nx][ny] - t[x][y]) // 4
    for i in range(n):
        for j in range(n):
            t[i][j] = temp[i][j]


def air_reduce():

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                if t[i][j]:
                    t[i][j] -= 1


def more_than_k():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and t[i][j] < k:
                return False
    return True


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
w = [[[False]*4 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, s = map(int, input().split())
    if s == 0:
        # 위
        w[x-1][y-1][s+1] = True
        # 아래
        w[x-2][y-1][s+3] = True
    else:
        # 왼쪽
        w[x-1][y-1][s-1] = True
        # 오른쪽
        w[x-1][y-2][s+1] = True
t = [[0]*n for _ in range(n)]
for ans in range(1, 101):

    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2:
                # 바람 전달
                air = air_con(i, j, a[i][j]-2)

                # 바람 전달 후 최종 상태.
                for u in range(n):
                    for v in range(n):
                        t[u][v] += air[u][v]

    air_mix()
    air_reduce()
    if more_than_k():
        print(ans)
        break

    else:
        if ans == 100:
            print(-1)
