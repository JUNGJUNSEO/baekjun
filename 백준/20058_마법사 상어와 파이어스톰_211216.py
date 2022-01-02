n, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(2 ** n)]
size = list(map(int, input().split()))
for s in size:

    for i in range(16):
        x, y = i // 4, i % 4
        t = [[0] * (2**s) for _ in range(2**s)]
        num = 0
        for j in range(x):
            for k in range(y):
                tx, ty = num // 2, num % 2
                t[tx][ty] = a[j][k]
                num += 1
        t = zip(*t)
        for j in range(x):
            for k in range(y): 
                a[j][k] = a[tx][ty]