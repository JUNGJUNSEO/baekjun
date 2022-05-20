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
                if a[nx][ny] == 1 and check[nx][ny] < 0:
                    q.append((nx, ny))
                    check[nx][ny] = num
                    cnt += 1
    return cnt


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[-1]*m for _ in range(n)]
group = dict()
num = 0
ans = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and check[i][j] < 0:
            group[num] = bfs(i, j, num)
            num += 1

for x in range(n):
    for y in range(m):
        temp = 0
        s = set()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and not check[nx][ny] in s:
                    temp += group[check[nx][ny]]
                    s.add(check[nx][ny])
        ans = max(ans, temp)

print(ans+1)
