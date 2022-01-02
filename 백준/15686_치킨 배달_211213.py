import sys


def dist(chicken):
    chicken_dis = 0
    for hx, hy in house:
        d = list()
        for cx, cy in chicken:
            d.append(abs(hx - cx) + abs(hy - cy))
        chicken_dis += min(d)
    return chicken_dis


def go(m, index, store):
    global ans
    if m == 0:
        ans = min(ans, dist(store))
        return
    for i in range(index, len(chicken)):
        go(m - 1, i + 1, store + [chicken[i]])


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
house = list()
chicken = list()
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            house.append((i, j))
        if a[i][j] == 2:
            chicken.append((i, j))
ans = sys.maxsize
go(m, 0, [])
print(ans)
