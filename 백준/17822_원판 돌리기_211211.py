from collections import deque
import copy
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    check[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], (y+dy[i]) % m
        if 0 <= nx < n and 0 <= ny < m:
            if a[x][y] == a[nx][ny] and not check[nx][ny]:
                temp[x][y] = 0
                temp[nx][ny] = 0
                bfs(nx, ny)


n, m, t = map(int, input().split())
a = [deque(map(int, input().split())) for _ in range(n)]
for _ in range(t):
    x, d, k = map(int, input().split())
    for num in range(1, 50):
        x1 = x*num
        if x1 > n:
            break
        if d == 0:
            a[x1-1].rotate(k)
        else:
            a[x1-1].rotate(-k)

    temp = copy.deepcopy(a)
    q = deque()
    q.append((0, 0))
    check = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] and not check[i][j]:
                bfs(i, j)
    for i in range(n):
        print(temp[i])
    if not check:
        s, cnt, t = 0, 0, list()
        for i in range(n):
            for j in range(m):
                if temp[i][j]:
                    s += temp[i][j]
                    cnt += 1
                    t.append((i, j))
        if s == 0:
            break
        ave = s/cnt
        for x, y in t:
            if temp[x][y] > ave:
                temp[x][y] -= 1
            elif temp[x][y] < ave:
                temp[x][y] += 1
    a = temp
ans = 0
for i in range(n):
    ans += sum(a[i])
print(ans)
