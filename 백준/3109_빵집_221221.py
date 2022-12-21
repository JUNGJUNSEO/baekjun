import sys
input = sys.stdin.readline

dx = [-1, 0, 1]


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def dfs(x, y):

    if y == c-1:
        return True

    check[x][y] = True

    for i in range(3):
        nx, ny = x + dx[i], y + 1

        if not in_range(nx, ny):
            continue
        if a[nx][ny] == 'x' or check[nx][ny]:
            continue

        if dfs(nx, ny):
            return True


r, c = map(int, input().split())
a = [input() for _ in range(r)]
check = [[False] * c for _ in range(r)]
cnt = 0

for i in range(r):
    if a[i][0] == '.':
        if dfs(i, 0):
            cnt += 1

print(cnt)
