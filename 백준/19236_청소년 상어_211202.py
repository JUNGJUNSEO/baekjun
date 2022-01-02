import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def fish(sx, sy, b, f):
    for i in range(16):
        if f[i]:
            for _ in range(8):
                x, y = f[i]
                nx, ny = x+dx[b[x][y][1]-1], y+dy[b[x][y][1]-1]
                if 0 <= nx < 4 and 0 <= ny < 4 and not(nx == sx and ny == sy):
                    if f[b[nx][ny][0]-1]:
                        f[i], f[b[nx][ny][0]-1] = f[b[nx][ny][0]-1], f[i]
                    else:
                        f[i] = (nx, ny)
                    b[nx][ny], b[x][y] = b[x][y], b[nx][ny]
                    break
                else:
                    b[x][y][1] = (b[x][y][1]+1) % 8
    return b, f


def shark(x, y, b, f):
    f[b[x][y][0]-1] = ()
    b, f = fish(x, y, b, f)
    ans, temp = b[x][y][0], b[x][y][0]
    for i in range(1, 4):
        nx, ny = x+dx[b[x][y][1]-1]*i, y+dy[b[x][y][1]-1]*i
        if 0 <= nx < 4 and 0 <= ny < 4 and f[b[nx][ny][0]-1]:
            ans = max(ans, temp+shark(nx, ny, copy.deepcopy(b), f.copy()))
    return ans


a = [list(map(int, input().split())) for _ in range(4)]
b = [[] for _ in range(4)]
f = [()]*16
for i in range(4):
    for j in range(2, 10, 2):
        x, y = a[i][j-2:j]
        b[i].append([x, y])
        f[x-1] = (i, int(j/2)-1)
print(shark(0, 0, b, f))
