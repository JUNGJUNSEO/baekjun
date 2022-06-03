import sys
input = sys.stdin.readline
dx_p = [0, 1, 0, -1]
dy_p = [1, 0, -1, 0]
dx_m = [1, 0, -1, 0]
dy_m = [0, 1, 0, -1]

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    d //= 45
    x, y, l = 0, 0, n//2
    if d > 0:
        dx, dy = dx_p, dy_p
    else:
        dx, dy = dx_m, dy_m

    for _ in range(abs(d)):
        for s in range(n//2):
            nx, ny, nl = x+s, y+s, l-s
            temp = a[nx][ny]
            for i in range(4):
                for _ in range(2):
                    nx, ny = nx+dx[i]*nl, ny+dy[i]*nl
                    a[nx][ny], temp = temp, a[nx][ny]
        x, y, l = 0, 0, n//2

    for i in range(n):
        print(' '.join(map(str, a[i])))
