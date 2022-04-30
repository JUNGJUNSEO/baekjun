from collections import deque
import copy

dir = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}
dir_xy = {v: k for k, v in dir.items()}


def bfs(x, y, d):
    dx, dy = dir[d][0], dir[d][1]
    x, y = x+dx, y+dy
    q = deque()
    q.append((x, y, 5))
    temp = [[0]*c for _ in range(r)]
    temp[x][y] = 5
    res[x][y] += 5
    while q:
        x, y, t = q.popleft()
        for idx in [0, -1, 1]:
            nt = t-1
            if d == 0 or d == 1:
                nx, ny = x+idx, y+dir[d][1]
            else:
                nx, ny = x+dir[d][0], y+idx
            if 0 <= nx < r and 0 <= ny < c and nt > 0:
                if temp[nx][ny] == 0 and not wall[d][nx][ny]:
                    if idx != 0:
                        if (d == 0 or d == 1) and wall[dir_xy[(idx, 0)]][nx][y]:
                            continue
                        if (d == 2 or d == 3) and wall[dir_xy[(0, idx)]][x][ny]:
                            continue
                    temp[nx][ny] = nt
                    res[nx][ny] = res[nx][ny] + nt
                    q.append((nx, ny, nt))


def control():

    lst = copy.deepcopy(res)
    for x in range(r):
        for y in range(c):
            for i in range(4):
                dx, dy = dir[i]
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c and not wall[dir_xy[(dx, dy)]][nx][ny]:
                    if res[x][y] > res[nx][ny]:
                        temp = abs(res[x][y]-res[nx][ny])//4
                        lst[x][y] -= temp
                        lst[nx][ny] += temp

    return lst


def disappear():

    x, y = 0, 0
    for d in [3, 0, 2, 1]:
        dx, dy = dir[d][0], dir[d][1]
        while True:
            if 0 <= x+dx < r and 0 <= y+dy < c:
                x, y = x+dx, y+dy
                if res[x][y] > 0:
                    res[x][y] -= 1
            else:
                break


def check():
    for x, y in loc_invest:
        if res[x][y] < k:
            return False
    return True


r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
w = int(input())
wall = [[[False]*c for _ in range(r)] for _ in range(4)]
for _ in range(w):
    x, y, t = map(int, input().split())
    x, y = x-1, y-1
    if t == 0:
        wall[2][x-1][y] = wall[3][x][y] = True
    else:
        wall[0][x][y+1] = wall[1][x][y] = True
res = [[0]*c for _ in range(r)]
loc_blower = list()
loc_invest = list()
for i in range(r):
    for j in range(c):
        if 1 <= a[i][j] < 5:
            loc_blower.append((i, j))
        if a[i][j] == 5:
            loc_invest.append((i, j))

ans = 0
while ans < 100:
    ans += 1
    for x, y in loc_blower:
        bfs(x, y, a[x][y]-1)
    res = control()
    disappear()
    if check():
        print(ans)
        exit()
print(101)
