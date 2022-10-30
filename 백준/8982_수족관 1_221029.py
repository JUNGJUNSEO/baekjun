def drain(x, h1, h2):

    for nx in range(x, len(a)):

        if h1 > a[nx]:
            h1 = a[nx]

        a[nx] -= h1

    for nx in range(x-1, -1, -1):

        if h2 > a[nx]:
            h2 = a[nx]

        a[nx] -= h2


n = int(input())
a = []
h, w = 0, 0

for i in range(n):

    x, y = map(int, input().split())

    if (i % 2) == 1:
        w = x
        h = y

    else:
        for _ in range(x - w):
            a.append(h)

k = int(input())

for _ in range(k):
    x1, _, x2, _ = map(int, input().split())
    x = (x2 + x1) // 2

    drain(x, a[x], a[x])

print(sum(a))
