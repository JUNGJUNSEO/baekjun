from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(ox, oy):
    check = [[False] * n for _ in range(n)]
    q, block, block_color = deque(), list(), list()
    check[ox][oy] = True
    q.append((ox, oy))
    block.append((ox, oy))
    block_color.append((ox, oy))
    cnt, cnt0 = 1, 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not check[nx][ny]:
                    if a[nx][ny] == a[ox][oy] or not a[nx][ny]:
                        q.append((nx, ny))
                        block.append((nx, ny))
                        check[nx][ny] = True
                        cnt += 1
                    if a[nx][ny] == a[ox][oy]:
                        block_color.append((nx, ny))
                    if not a[nx][ny]:
                        cnt0 += 1
    block_color.sort()
    return [cnt, cnt0, block_color[0][0], block_color[0][1], block]


def gravity():
    for x in reversed(range(n - 1)):
        for y in range(n):
            s = 0
            if a[x][y] >= 0:
                for i in range(1, n):
                    if 0 <= x + i < n and a[x + i][y] == -2:
                        s += 1
                    else:
                        break
            a[x + s][y], a[x][y] = a[x][y], a[x + s][y]


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while True:
    blocks = list()
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0:
                block = bfs(i, j)
                if block[0] > 1:
                    blocks.append(block)
    if not blocks:
        break
    blocks.sort()
    ans += blocks[-1][0] ** 2
    block = blocks[-1][4]
    for x, y in block:
        a[x][y] = -2
    gravity()
    a = list(map(list, reversed(list(zip(*a)))))
    gravity()
print(ans)