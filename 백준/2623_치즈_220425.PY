from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    visit = [[False]*m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny]:
                    if a[nx][ny] == 0:
                        q.append((nx, ny))
                    else:
                        a[nx][ny] = 0
                        cnt += 1
                    visit[nx][ny] = True
    return cnt


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
time = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            cnt += 1
            
while True:

    temp = bfs(0, 0)
    if temp > 0:
        cnt = temp
        time += 1
    else:
        break

print(time)
print(cnt)