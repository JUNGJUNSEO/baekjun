dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, num, cnt):
    if cnt == 5:
        ans.append(num)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + str(a[nx][ny]), cnt + 1)


a = [list(map(int, input().split())) for _ in range(5)]
ans = list()
for i in range(5):
    for j in range(5):
        dfs(i, j, str(a[i][j]), 0)
print(len(set(ans)))
