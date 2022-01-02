from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny]:
                    continue
                if a[nx][ny] == '.':
                    check[nx][ny] = True
                    q.append((nx, ny))
                elif a[nx][ny] == 'S':
                    if a[x][y] == 'W':
                        return 0
                    a[x][y] = 'D'
    return 1


n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
check = [[False]*m for _ in range(n)]
ans = 1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'W':
            check[i][j] = True
            ans = bfs(i, j)
if ans == 1:
    print(ans)
    for i in range(n):
        print(''.join(a[i]))
else:
    print(ans)
