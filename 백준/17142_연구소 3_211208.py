from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(s):

    cnt = [[-1]*n for _ in range(n)]
    for x, y in s:
        cnt[x][y] = 0
    q1 = deque(s)
    q2 = deque(s)
    while q1:
        x, y = q1.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and cnt[nx][ny] < 0:
                if a[nx][ny] == 2:
                    cnt[nx][ny] = cnt[x][y]
                    q1.append((nx, ny))
                    q2.append((nx, ny))
    while q2:
        x, y = q2.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and cnt[nx][ny] < 0:
                if a[nx][ny] == 0:
                    cnt[nx][ny] = cnt[x][y]+1
                    q2.append((nx, ny))
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                if cnt[i][j] < 0:
                    return -1
                else:
                    ans = max(ans, cnt[i][j])
    return ans


def go(index, l, s):
    if l == 0:
        temp = bfs(s)
        if temp >= 0:
            ans.append(temp)
        return
    for i in range(index, len(b)):
        go(i+1, l-1, s+[b[i]])


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
