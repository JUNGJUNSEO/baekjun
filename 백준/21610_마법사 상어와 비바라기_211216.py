from collections import deque

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cloud = deque([[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]])
check = [[False] * n for _ in range(n)]
for _ in range(m):
    d, s = map(int, input().split())
    for i in range(len(cloud)):
        x, y = cloud.popleft()
        nx, ny = (x + (n + dx[d - 1]) * s) % n, (y + (n + dy[d - 1]) * s) % n
        a[nx][ny] += 1
        check[nx][ny] = True
        cloud.append([nx, ny])
    while cloud:
        x, y = cloud.pop()
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[2 * i + 1], y + dy[2 * i + 1]
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny]:
                cnt += 1
        a[x][y] += cnt
    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2 and not check[i][j]:
                cloud.append([i, j])
                a[i][j] -= 2
            if check[i][j]:
                check[i][j] = False
print(sum(sum(s) for s in a))
