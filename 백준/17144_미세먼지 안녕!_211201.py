r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(t):
    l = []
    dust = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if a[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < r and 0 <= ny < c:
                        if a[nx][ny] >= 0:
                            dust[nx][ny] += int(a[x][y]/5)
                            cnt += 1
                dust[x][y] += a[x][y]-int(a[x][y]/5)*cnt
            elif a[x][y] < 0:
                dust[x][y] = a[x][y]
                l.append(x)
    l1, l2 = l
    for i in range(l1-1, 0, -1):
        dust[i][0] = dust[i-1][0]
    for i in range(c-1):
        dust[0][i] = dust[0][i+1]
    for i in range(l1):
        dust[i][c-1] = dust[i+1][c-1]
    for i in range(c-1, 0, -1):
        dust[l1][i] = dust[l1][i-1]
    dust[l1][1] = 0

    for i in range(l2+1, r-1):
        dust[i][0] = dust[i+1][0]
    for i in range(c-1):
        dust[r-1][i] = dust[r-1][i+1]
    for i in range(r-1, l2, -1):
        dust[i][c-1] = dust[i-1][c-1]
    for i in range(c-1, 1, -1):
        dust[l2][i] = dust[l2][i-1]
    dust[l2][1] = 0

    a = dust
ans = 2
for i in range(r):
    for j in range(c):
        ans += a[i][j]
print(ans)
