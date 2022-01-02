from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    temp = list()
    temp.append((x, y))
    check[x][y] = True
    sum = a[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not check[nx][ny] and l <= abs(a[x][y]-a[nx][ny]) <= r:
                    check[nx][ny] = True
                    q.append((nx, ny))
                    temp.append((nx, ny))
                    sum += a[nx][ny]
    return temp, sum


n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while True:
    check = [[False]*n for _ in range(n)]
    T = False
    for x in range(n):
        for y in range(n):
            if not check[x][y]:
                temp, sum = bfs(x, y)
                res = int(sum/len(temp))
                if len(temp) > 1:
                    T = True
                for i, j in temp:
                    a[i][j] = res
    if T:
        ans += 1
    else:
        break
print(ans)
