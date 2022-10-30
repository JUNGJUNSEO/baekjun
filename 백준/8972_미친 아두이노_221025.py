dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
Inf = int(1e9)


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def c_move(zx, zy):

    cnt = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if grid[x][y] == 'R':

                min_dist = Inf
                mx, my = x, y

                for i in range(9):
                    nx, ny = x + dx[i], y + dy[i]
                    dist = abs(zx-nx) + abs(zy-ny)

                    if min_dist > dist:
                        min_dist = dist
                        mx, my = nx, ny

                cnt[mx][my] += 1

    for x in range(r):
        for y in range(c):
            if cnt[x][y] > 0:
                if next_grid[x][y] == 'I':
                    return False
                if cnt[x][y] == 1:
                    next_grid[x][y] = 'R'

    return True


def z_move(d):

    for x in range(r):
        for y in range(c):
            if grid[x][y] == 'I':

                nx, ny = x + dx[d], y + dy[d]

                if grid[nx][ny] == 'R':
                    return -1, -1
                else:
                    next_grid[nx][ny] = 'I'
                    return nx, ny


r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
next_grid = [['.'] * c for _ in range(r)]

for idx, d in enumerate(list(map(int, input()))):

    for i in range(r):
        for j in range(c):
            next_grid[i][j] = '.'

    zx, zy = z_move(d - 1)

    if zx == -1 and zy == -1:
        print(f'kraj {idx + 1}')
        exit()

    if not c_move(zx, zy):
        print(f'kraj {idx + 1}')
        exit()

    for i in range(r):
        for j in range(c):
            grid[i][j] = next_grid[i][j]


for i in range(r):
    print(''.join(grid[i]))
