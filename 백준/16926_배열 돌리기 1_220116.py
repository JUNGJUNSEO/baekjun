dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def rotate(x, y, *l):

    if min(l) == 0:
        return

    lst = list()
    for i in range(4):
        for _ in range(l[i % 2]-1):
            x, y = x+dx[i], y+dy[i]
            lst.append((x, y))

    length = len(lst)
    for i in range(length):
        ox, oy = lst[i]
        nx, ny = lst[(i+r) % length]
        result[nx][ny] = a[ox][oy]

    rotate(x+1, y+1, l[0]-2, l[1]-2)


n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*m for _ in range(n)]

rotate(0, 0, n, m)

for i in range(n):
    print(' '.join(map(str, result[i])))
