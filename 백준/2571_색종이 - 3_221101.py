n = int(input())
a = [[0] * 100 for _ in range(100)]
p = [[0] * 100 for _ in range(100)]

for _ in range(n):

    x, y = map(int, input().split())
    x, y = x - 1, y - 1

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            a[i][j] = 1

for j in range(100):

    s = 0

    for i in range(100):

        if not a[i][j]:
            s = 0
            continue

        s += a[i][j]
        p[i][j] = s

ans = 0

for x in range(100):
    for y in range(100):

        h, w = p[x][y], 0

        for i in range(100):

            ny = y + i

            if not (ny < 100):
                break
            if h == 0:
                break
            else:
                if h > p[x][ny]:
                    h = p[x][ny]
                w += 1

            ans = max(ans, h * w)

print(ans)
