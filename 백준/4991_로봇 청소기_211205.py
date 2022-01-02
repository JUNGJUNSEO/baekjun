from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    t = list()
    q.append((x, y))
    cnt = [[-1]*m for _ in range(n)]
    cnt[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and cnt[nx][ny] < 0 and a[nx][ny] != 'x':
                cnt[nx][ny] = cnt[x][y]+1
                q.append((nx, ny))
                if a[nx][ny] == '*':
                    t.append((nx, ny, cnt[nx][ny]))
    return t


def go(l, x, y, res):
    global ans
    if l == 0:
        ans = min(ans, res)
        return
    for x, y, dis in b[x][y]:
        if not check[x][y]:
            check[x][y] = True
            go(l-1, x, y, res+dis)
            check[x][y] = False


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    a = [list(input()) for _ in range(n)]
    b = [[[]for _ in range(m)] for _ in range(n)]
    l = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                b[i][j] += bfs(i, j)
                l += 1
            if a[i][j] == 'o':
                b[i][j] += bfs(i, j)
                x, y = i, j
    check = [[False]*m for _ in range(n)]
    ans = 100000
    go(l, x, y, 0)
    if ans == 100000:
        print(-1)
    else:
        print(ans)
