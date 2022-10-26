dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
Inf = int(1e9)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def pin_count():

    cnt = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'o':
                cnt += 1

    return cnt


def play_game(cnt):
    global pin_cnt, move_cnt

    temp = pin_count()

    if pin_cnt > temp:

        pin_cnt = temp
        move_cnt = cnt

    elif pin_cnt == temp:
        move_cnt = min(move_cnt, cnt)

    for x in range(n):
        for y in range(m):
            if grid[x][y] == 'o':
                for i in range(4):
                    nx, ny = x + dx[i], y+dy[i]

                    if not in_range(nx, ny):
                        continue

                    if grid[nx][ny] == 'o':

                        jx, jy = nx + dx[i], ny + dy[i]

                        if not in_range(jx, jy):
                            continue

                        if grid[jx][jy] == '.':
                            t1, t2, t3 = grid[x][y], grid[nx][ny], grid[jx][jy]
                            grid[x][y], grid[nx][ny], grid[jx][jy] = '.', '.', 'o'
                            play_game(cnt + 1)
                            grid[x][y], grid[nx][ny], grid[jx][jy] = t1, t2, t3


t = int(input())

for _ in range(t):

    n, m = 5, 9
    grid = [list(input()) for _ in range(n)]
    pin_cnt, move_cnt = pin_count(), Inf
    play_game(0)
    print(pin_cnt, move_cnt if move_cnt != Inf else 0)

    try:
        input()
    except:
        break
