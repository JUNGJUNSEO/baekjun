from collections import deque, defaultdict
import copy
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def rotate():
    res = [[0]*n for _ in range(n)]
    x, y = n//2, n//2
    for i in range(n):
        res[n-y-1][i] = a[i][y]
    for j in range(n):
        res[n-j-1][x] = a[x][j]

    for sx in [0, n//2+1]:
        for sy in [0, n//2+1]:
            for x in range(sx, sx+n//2):
                for y in range(sy, sy+n//2):
                    ox, oy = x-sx, y-sy
                    rx, ry = oy, n//2-ox-1
                    res[rx+sx][ry+sy] = a[x][y]

    return res


def bfs(i, j, num):
    q = deque()
    q.append([i, j])
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] < 0 and a[nx][ny] == num:
                    g[nx][ny] = g[x][y]
                    cnt += 1
                    q.append([nx, ny])
    return cnt


def calc():
    d_cnt = {}
    d_num = {}
    d_nav = defaultdict(int)
    total = 0

    num = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] < 0:
                g[i][j] = num
                d_cnt[num] = bfs(i, j, a[i][j])
                d_num[num] = a[i][j]
                num += 1

    for i in range(n):
        for j in range(n-1):
            if g[i][j] != g[i][j+1]:
                d_nav[tuple(sorted([g[i][j], g[i][j+1]]))] += 1

    for j in range(n):
        for i in range(n-1):
            if g[i][j] != g[i+1][j]:
                d_nav[tuple(sorted([g[i][j], g[i+1][j]]))] += 1

    for key, value in d_nav.items():
        n1, n2 = key
        total += (d_cnt[n1]+d_cnt[n2])*d_num[n1]*d_num[n2]*value

    return total


answer = 0
for _ in range(4):
    g = [[-1]*n for _ in range(n)]
    answer += calc()
    a = rotate()
print(answer)
