import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def magic(a, l):
    m, s, p = 0, 0, True
    for j in range(l):
        m += a[j][0]
        s += a[j][1]
        if a[0][2] % 2 != a[j][2] % 2:
            p = False
    if p:
        dir = [0, 2, 4, 6]
    else:
        dir = [1, 3, 5, 7]
    return int(m / 5), int(s / l), dir


n, m, k = map(int, input().split())
shark_a1 = [[list() for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, m, s, d = map(int, input().split())
    shark_a1[r - 1][c - 1].append([m, s, d])

for _ in range(k):

    shark_a2 = [[list() for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            while shark_a1[x][y]:
                m, s, d = shark_a1[x][y].pop()
                nx, ny = (x + (n + dx[d]) * s) % n, (y + (n + dy[d]) * s) % n
                shark_a2[nx][ny].append([m, s, d])

    shark_a3 = copy.deepcopy(shark_a2)
    for x in range(n):
        for y in range(n):
            length = len(shark_a2[x][y])
            if length >= 2:
                m, s, dir = magic(shark_a2[x][y], length)
                shark_a3[x][y] = list()
                if m > 0:
                    for num in range(4):
                        shark_a3[x][y].append((m, s, dir[num]))
    shark_a1 = shark_a3

ans = 0
for i in range(n):
    for j in range(n):
        while shark_a1[i][j]:
            ans += shark_a1[i][j].pop()[0]
print(ans)
