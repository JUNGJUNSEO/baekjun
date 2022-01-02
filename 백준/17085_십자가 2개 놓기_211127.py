dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def go(x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not(0 <= nx < n and 0 <= ny < m) or a[nx][ny] == '.':
            return


n, m = map(int, input().split())
a = [input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == '#':
            go(i, j)
