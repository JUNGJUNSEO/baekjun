import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
r, c, m = map(int, input().split())
a = [[[]for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    a[x-1][y-1] = [s, d, z]
ans = 0
for l in range(c):
    for i in range(r):
        if a[i][l]:  # 0 바꿔주기
            ans += a[i][l][2]
            a[i][l] = []
            break
    temp = [[[]for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if a[i][j]:
                s, d, z = a[i][j][0], a[i][j][1], a[i][j][2]
                if d == 1 or d == 2:
                    s = s % ((r-1)*2)
                if d == 3 or d == 4:
                    s = s % ((c-1)*2)
                nx, ny = i+dx[d-1]*s, j+dy[d-1]*s
                print(i, j)
                if d == 1:
                    if (nx / ((r-1)*2)) % 2 == 1:
                        d += 1
                    nx = (nx+((r-1)*2)) % ((r-1)*2)

                if d == 2:
                    if (nx / ((r-1)*2)) % 2 == 1:
                        d -= 1
                    nx = (((r-1)*2) - nx) % ((r-1)*2)

                if d == 3:
                    if (ny / ((c-1)*2)) % 2 == 1:
                        d += 1
                    ny = (((c-1)*2) - ny) % ((c-1)*2)

                if d == 4:
                    if (ny / ((c-1)*2)) % 2 == 1:
                        d -= 1
                    ny = (ny+((c-1)*2)) % ((c-1)*2)
                print(nx, ny)
                # nx, ny = i, j
                # for _ in range(s):
                #     nx, ny = nx+dx[d-1], ny+dy[d-1]
                #     if not (0 <= nx < r and 0 <= ny < c):
                #         if d % 2 == 1:
                #             d += 1
                #         else:
                #             d -= 1
                #         nx, ny = nx+dx[d-1]*2, ny+dy[d-1]*2
                if temp[nx][ny]:
                    if temp[nx][ny][2] < z:
                        temp[nx][ny] = [s, d, z]
                else:
                    temp[nx][ny] = [s, d, z]
    a = copy.deepcopy(temp)
print(ans)
