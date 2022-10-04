import copy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def mons_move():
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    res = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for d in live_mon[x][y]:
                check = False
                for i in range(9):
                    nx, ny = x+dx[(d+i) % 8], y+dy[(d+i) % 8]
                    if 0 <= nx < n and 0 <= ny < n and not dead_mon[nx][ny] and not (px == nx and py == ny):
                        res[nx][ny].append((d+i) % 8)
                        check = True
                        break
                if not check:
                    res[x][y].append(d)
    return res


def get_kiiled_num(d1, d2, d3):
    x, y = px, py
    s = 0
    temp = []

    for i in [d1, d2, d3]:
        x, y = x+dx[i], y+dy[i]
        if 0 <= x < n and 0 <= y < n:
            if [x, y] not in temp:
                s += len(live_mon[x][y])
                temp.append([x, y])
        else:
            return -1
    return s


def pack_move():
    global px, py

    # best 경로 설정
    MAX, path = -1, (-1, -1, -1)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                num = get_kiiled_num(i, j, k)
                if num > MAX:
                    MAX = num
                    path = (i, j, k)

    # 몬스터 시체 소멸.
    for i in range(n):
        for j in range(n):
            temp = []
            for dead in dead_mon[i][j]:
                cnt = dead-1
                if cnt > 0:
                    temp.append(cnt)
            dead_mon[i][j] = temp

    # 팩맨 이동.
    for i in path:
        px, py = px+dx[i], py+dy[i]
        if live_mon[px][py]:
            live_mon[px][py] = []
            dead_mon[px][py].append(2)


def dupl_comp():
    for i in range(n):
        for j in range(n):
            if dupl_mon[i][j]:
                for d in dupl_mon[i][j]:
                    live_mon[i][j].append(d)


m, t = map(int, input().split())
px, py = map(int, input().split())
px, py = px-1, py-1
n = 4
live_mon = [[[] for _ in range(n)] for _ in range(n)]
dead_mon = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    mx, my, d = map(int, input().split())
    live_mon[mx-1][my-1].append(d-1)
for _ in range(t):
    dupl_mon = copy.deepcopy(live_mon)
    live_mon = mons_move()
    pack_move()
    dupl_comp()

ans = 0
for i in range(n):
    for j in range(n):
        if live_mon[i][j]:
            ans += len(live_mon[i][j])

print(ans)
