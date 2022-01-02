dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def blue(num, x, y, s, d):
    # 비트 연산자 이용할 것.
    d ^= 1
    nx, ny = x + dx[d], y + dy[d]
    horse[num][3] = d
    if 0 <= nx < n and 0 <= ny < n:
        if not a[nx][ny] == 2:
            return color(num, x, y, s, d)


def color(num, x, y, s, d):
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] == 2:
            return blue(num, x, y, s, d)

        if a[nx][ny] == 0:
            l[nx][ny] += l[x][y][s:]

        if a[nx][ny] == 1:
            l[nx][ny] += l[x][y][s:][-1::-1]
        l[x][y] = l[x][y][0:s]
    else:
        return blue(num, x, y, s, d)

    for index, num in enumerate(l[nx][ny]):
        horse[num][0:3] = [nx, ny, index]

    if len(l[nx][ny]) >= 4:
        print(ans)
        exit()


n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
l = [[[] for _ in range(n)] for _ in range(n)]
horse = list()
for i in range(k):
    x, y, d = map(int, input().split())
    l[x - 1][y - 1].append(i)
    horse.append([x - 1, y - 1, 0, d - 1])
ans = 0
while ans < 1000:
    ans += 1
    for i in range(k):
        x, y, s, d = horse[i]
        color(i, x, y, s, d)
print(-1)
