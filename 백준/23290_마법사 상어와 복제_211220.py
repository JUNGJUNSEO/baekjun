dx_f = [0, -1, -1, -1, 0, 1, 1, 1]
dy_f = [-1, -1, 0, 1, 1, 1, 0, -1]
dx_s = [-1, 0, 1, 0]
dy_s = [0, -1, 0, 1]


def s_move(l, eat, sx, sy, arr):
    global sx_n, sy_n, max_eat, f_remove
    if l == 0:
        if eat > max_eat:
            sx_n, sy_n, max_eat = sx, sy, eat
            f_remove = arr
        return
    for i in range(4):
        nx, ny = sx + dx_s[i], sy + dy_s[i]
        if 0 <= nx < 4 and 0 <= ny < 4 and not visit[nx][ny]:
            visit[nx][ny] = True
            s_move(l - 1, eat + len(a_copy[nx][ny]), nx, ny, arr + [[nx, ny]])
            visit[nx][ny] = False


m, s = map(int, input().split())
a = [[list() for _ in range(4)] for _ in range(4)]
for _ in range(m):
    fx, fy, d = map(int, input().split())
    a[fx - 1][fy - 1].append(d - 1)
sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1
smell = [[0] * 4 for _ in range(4)]

for _ in range(s):
    a_copy = [[list() for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in a[x][y]:
                for _ in range(8):
                    nx, ny = x + dx_f[(d + 8) % 8], y + dy_f[(d + 8) % 8]
                    if (
                        0 <= nx < 4
                        and 0 <= ny < 4
                        and not smell[nx][ny]
                        and not (nx == sx and ny == sy)
                    ):
                        a_copy[nx][ny].append((d + 8) % 8)
                        break
                    else:
                        d -= 1

    sx_n, sy_n, max_eat, f_remove = sx, sy, len(a_copy[sx][sy]), list()
    visit = [[False] * 4 for _ in range(4)]
    visit[sx][sy] = True
    s_move(3, len(a_copy[sx][sy]), sx, sy, list(a_copy[sx][sy]))
    sx, sy = sx_n, sy_n

    for x in range(4):
        for y in range(4):
            if smell[x][y]:
                smell[x][y] -= 1
    for x, y in f_remove:
        if a_copy[x][y]:
            a_copy[x][y] = list()
            smell[x][y] = 2

    for x in range(4):
        for y in range(4):
            a[x][y] += a_copy[x][y]
ans = 0
for i in range(4):
    for j in range(4):
        ans += len(a[i][j])
print(ans)
