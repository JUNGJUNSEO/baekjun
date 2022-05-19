from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(q):
    global ans

    while q:
        x, y, s = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and a[nx][ny] == '.':
                    q.append((nx, ny, s))
                    visit[nx][ny] = visit[x][y] + 1
            else:
                if s == 'J':
                    return visit[x][y]


n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
visit = [[0]*m for _ in range(n)]


q = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == 'J':
            visit[i][j] = 1
            q.append((i, j, 'J'))
        if a[i][j] == 'F':
            visit[i][j] = 1
            q.appendleft((i, j, 'F'))

ans = bfs(q)
if ans:
    print(ans)
else:
    print('IMPOSSIBLE')
