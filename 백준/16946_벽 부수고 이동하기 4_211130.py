from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, num):
    check[x][y] = num
    q = deque()
    q.append((x, y))
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0 and check[nx][ny] < 0:
                    check[nx][ny] = num
                    q.append((nx, ny))
                    cnt += 1
    return cnt


n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
check = [[-1]*m for _ in range(n)]
num = 0
size = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] < 0:
            size.append(bfs(i, j, num))
            num += 1

ans = [[0]*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if a[x][y] == 1:
            temp = 1
            lst = list()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0 and check[nx][ny] not in lst:
                        temp += size[check[nx][ny]]
                        lst.append(check[nx][ny])
            ans[x][y] = temp % 10
for i in range(n):
    print(''.join(map(str, ans[i])))
