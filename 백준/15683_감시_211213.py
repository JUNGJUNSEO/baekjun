import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def see(dir, x, y, check):
    for i in dir:
        for s in range(1, 8):
            nx, ny = x + dx[i] * s, y + dy[i] * s
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 6:
                    break
                if not check[nx][ny]:
                    check[nx][ny] = True
            else:
                break


def go(index, l, check):
    global ans
    if index == l:
        cnt = 0
        for i in range(n):
            for j in range(m):
                if not check[i][j]:
                    cnt += 1
        ans = min(cnt, ans)
        return
    num, x, y = c[index]

    for i in range(4):
        check_copy = copy.deepcopy(check)
        if num == 1:
            dir = [i]
        elif num == 2:
            dir = [i, (i + 2) % 4]
        elif num == 3:
            dir = [i, (i + 1) % 4]
        elif num == 4:
            dir = [i, (i + 1) % 4, (i + 2) % 4]
        elif num == 5:
            dir = [0, 1, 2, 3]
        see(dir, x, y, check_copy)
        go(index + 1, l, check_copy)


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]
c = list()
for i in range(n):
    for j in range(m):
        if 0 < a[i][j] < 6:
            c.append([a[i][j], i, j])
            check[i][j] = True
        if a[i][j] == 6:
            check[i][j] = True
ans = 100
go(0, len(c), check)
print(ans)
