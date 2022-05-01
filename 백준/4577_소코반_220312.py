d = {'D': [1, 0], 'L': [0, -1], 'U': [-1, 0], 'R': [0, 1]}


def play(x, y, index, cnt):
    if index == l or cnt == 0:
        if a[x][y] == '.':
            a[x][y] = 'w'
        if a[x][y] == '+':
            a[x][y] = 'W'
        if cnt == 0:
            return 'complete'
        else:
            return 'incomplete'

    dx, dy = d[keys[index]]
    nx, ny = x+dx, y+dy
    if a[nx][ny] == '.' or a[nx][ny] == '+':
        return play(nx, ny, index+1, cnt)
    if a[nx][ny] == '#':
        return play(x, y, index+1, cnt)
    if a[nx][ny] == 'b' or a[nx][ny] == 'B':
        nnx, nny = nx+dx, ny+dy
        if a[nnx][nny] == '#' or a[nnx][nny] == 'b' or a[nnx][nny] == 'B':
            return play(x, y, index+1, cnt)
        if a[nnx][nny] == '.':
            a[nnx][nny] = 'b'
            if a[nx][ny] == 'b':
                a[nx][ny] = '.'
            else:
                a[nx][ny] = '+'
                cnt += 1
            return play(nx, ny, index+1, cnt)
        if a[nnx][nny] == '+':
            a[nnx][nny] = 'B'
            if a[nx][ny] == 'b':
                a[nx][ny] = '.'
            else:
                a[nx][ny] = '+'
                cnt += 1
            return play(nx, ny, index+1, cnt-1)


num = 0
while True:
    num += 1
    r, c = map(int, input().split())

    if r == 0 and c == 0:
        break

    a = [list(input()) for _ in range(r)]
    keys = list(input())
    sx, sy = 0, 0
    cnt = 0
    l = len(keys)
    for i in range(r):
        for j in range(c):
            if a[i][j] == 'w':
                sx, sy = i, j
                a[i][j] = '.'
            if a[i][j] == 'W':
                sx, sy = i, j
                a[i][j] = '+'
            if a[i][j] == '+':
                cnt += 1
    print(f'Game {num}: {play(sx, sy, 0, cnt)}')
    for i in range(r):
        print(''.join(a[i]))
