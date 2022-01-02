a = [[0] * 10 for _ in range(10)]
n = int(input())
for _ in range(n):
    t, x, y = map(int, input().split())
    while True:
        if a[x+1][y] == 0:
            a[x][y], a[x+1][y] = a[x+1][y], a[x][y]
        if a[x][y+1] == 0:
            a[x][y+1], a[x][y] = a[x][y], a[x][y+1]