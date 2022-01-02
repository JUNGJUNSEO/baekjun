dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
sand_shape = list()
sand = [
    (0, 0, 2, 0, 0),
    (0, 10, 7, 1, 0),
    (5, -1, 0, 0, 0),
    (0, 10, 7, 1, 0),
    (0, 0, 2, 0, 0),
]
sand_shape.append(sand)
for i in range(3):
    sand = list(reversed(list(zip(*sand))))
    sand_shape.append(sand)


def tornado(x, y, total, sand):
    global ans
    for i in range(5):
        for j in range(5):
            sx, sy = x + (i - 2), y + (j - 2)
            if sand[i][j] > 0:
                amount = int(total * sand[i][j] * 0.01)
                a[x][y] -= amount
                if 0 <= sx < n and 0 <= sy < n:
                    a[sx][sy] += amount
                else:
                    ans += amount
            elif sand[i][j] < 0:
                tx, ty = sx, sy
    if 0 <= tx < n and 0 <= ty < n:
        a[tx][ty] += a[x][y]
    else:
        ans += a[x][y]
    a[x][y] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
x, y = int(n / 2), int(n / 2)
ans, move = 0, 1
while True:
    for i in range(4):
        for _ in range(move % 2 + move // 2):
            x, y = x + dx[i], y + dy[i]
            if a[x][y]:
                tornado(x, y, a[x][y], sand_shape[i])
            if x == 0 and y == 0:
                print(ans)
                exit()
        move += 1
