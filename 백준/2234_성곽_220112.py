from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(x, y, num):
    q = deque()
    q.append((x, y))
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if check[nx][ny] < 0 and (a[x][y] & (1 << i)) == 0:
                    check[nx][ny] = num
                    q.append((nx, ny))
                    cnt += 1
    return cnt


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
check = [[-1]*n for _ in range(m)]
num = 0
room = dict()
for i in range(m):
    for j in range(n):
        if check[i][j] < 0:
            check[i][j] = num
            room[num] = bfs(i, j, num)
            num += 1
print(len(room))
print(max(room.values()))
ans = 0
for x in range(m):
    for y in range(n):
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if check[x][y] != check[nx][ny]:
                    ans = max(ans, room[check[x][y]]+room[check[nx][ny]])
print(ans)
