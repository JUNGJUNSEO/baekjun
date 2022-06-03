import copy

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    d //= 45

    for _ in range(abs(d) % 8):
        res = copy.deepcopy(a)

        for i in range(n):
            if d > 0:
                res[i][n//2], res[i][n-1-i], res[n//2][n-1-i], res[n-1 -
                                                                   i][n-1-i] = a[i][i], a[i][n//2], a[i][n-1-i], a[n//2][n-1-i]
            else:
                res[i][i], res[i][n//2], res[i][n-1-i], res[n//2][n-1 -
                                                                  i] = a[i][n//2], a[i][n-1-i], a[n//2][n-1-i], a[n-1-i][n-1-i]

        a = copy.deepcopy(res)

    for i in range(n):
        print(' '.join(map(str, a[i])))
