from collections import deque
import sys
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, z, day):
    q = deque()
    q.append((x, y, z, day))
    cnt[day][z][x][y] = 1
    while q:
        x, y, z, d = q.popleft()
        if d == 1:
            cnt[d][z][x][y] += 1
            q.append((x, y, z, d ^ 1))
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if d == 0 or d == 1:
                    if cnt[d][z][nx][ny] < 0 and a[nx][ny] == 0:
                        cnt[d][z][nx][ny] = cnt[d][z][x][y] + 1
                        q.append((nx, ny, z, d ^ 1))
                if d == 0 and z+1 <= k:
                    if cnt[d][z+1][nx][ny] < 0:
                        cnt[d][z+1][nx][ny] = cnt[d][z][x][y] + 1
                        q.append((nx, ny, z+1, d ^ 1))


n, m, k = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
cnt = [[[[-1]*m for _ in range(n)] for _ in range(k+1)] for _ in range(2)]
bfs(0, 0, 0, 0)
print(cnt)
ans = sys.maxsize
for i in range(k+1):
    if cnt[0][i][n-1][m-1] > 0:
        ans = min(ans, cnt[0][i][n-1][m-1])
print(ans if ans != sys.maxsize else -1)
