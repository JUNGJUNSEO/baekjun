import sys
input = sys.stdin.readline


def calc(a):
    global ans

    p = []
    s = 0

    for i in range(n):
        s += a[i]
        p.append(s)

    i1, i2 = 0, 1

    while i2 < n:

        ans = max(ans, (p[i2-1] - p[i1]) + 2 * (p[n-1] - p[i2]))

        i2 += 1


n = int(input())
a = list(map(int, input().split()))
ans = 0
calc(a)
calc(a[::-1])

print(max(ans, max(a[1:-1]) + sum(a[1:-1])))
