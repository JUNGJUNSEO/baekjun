from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(s):
    cnt = [[-1]*n for _ in range(n)]
    q = deque()
    for x, y in s:
        cnt[x][y] = 0
        q.append((x, y))
    time = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not a[nx][ny] == 1 and cnt[nx][ny] < 0:
                    cnt[nx][ny] = cnt[x][y]+1
                    q.append((nx, ny))
                    time = cnt[nx][ny]
    for i in range(n):
        for j in range(n):
            if cnt[i][j] < 0 and a[i][j] == 0:
                time = -1
    return time


def go(x, m, s):
    if m == 0:
        time = bfs(s)
        if time >= 0:
            ans.append(time)
        return
    for i in range(x, len(b)):
        go(i+1, m-1, s+[b[i]])


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = list()
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            b.append((i, j))
ans = []
go(0, m, [])
if ans:
    print(min(ans))
else:
    print(-1)
