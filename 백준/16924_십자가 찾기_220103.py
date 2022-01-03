import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = copy.deepcopy(a)
ans = list()
for x in range(n):
    for y in range(m):
        if a[x][y] == "*":
            s, check = 1, True
            lst = list()
            lst.append([x, y])
            while check:
                for i in range(4):
                    nx, ny = x + dx[i] * s, y + dy[i] * s
                    if 0 <= nx < n and 0 <= ny < m:
                        lst.append([nx, ny])
                        if a[nx][ny] == ".":
                            check = False
                            break
                    else:
                        check = False
                        break
                if check:
                    ans.append([x + 1, y + 1, s])
                    for bx, by in lst:
                        b[bx][by] = "."
                    s += 1
for i in range(n):
    for j in range(m):
        if b[i][j] == "*":
            print(-1)
            exit()
print(len(ans))
for x, y, s in ans:
    print(x, y, s)
