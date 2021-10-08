n, m = map(int, input().split())
a = [[] for _ in range(m+1)]
for _ in range(m):
    x, y, c = map(int, input().split())
    a[x].append([y, c])
    a[y].append([x, c])
s, e = map(int, input().split())
check = [False]*(n+1)

print(a)
