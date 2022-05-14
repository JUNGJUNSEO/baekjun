import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def rotate(n, m):
    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = s[i][j]
    return result


def paste(sx, sy):
    for i in range(sx, x+sx):
        for j in range(sy, y+sy):
            if s[i-sx][j-sy] == 1:
                a[i][j] = s[i-sx][j-sy]


def check(num):
    if num == n*m:
        return False
    sx, sy = num//m, num % m
    for i in range(sx, sx+x):
        for j in range(sy, sy+y):
            if not (0 <= i < n and 0 <= j < m):
                return check(num+1)
            else:
                if s[i-sx][j-sy] == 1 and a[i][j] == 1:
                    return check(num+1)

    paste(sx, sy)
    return True


n, m, k = map(int, input().split())
a = [[0]*m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(x)]
    for _ in range(4):
        if check(0):
            break
        else:
            s = rotate(x, y)
            x, y = y, x

print(sum(sum(a[i]) for i in range(n)))
