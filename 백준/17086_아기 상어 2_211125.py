from collections import deque

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(x, y):
    cnt = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((x, y))
    cnt[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if cnt[nx][ny] < 0:
                    q.append((nx, ny))
                    cnt[nx][ny] = cnt[x][y]+1
                if cnt[nx][ny] and a[nx][ny] == 1:
                    return cnt[nx][ny]-1


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            ans = max(bfs(i, j), ans)
print(ans)
