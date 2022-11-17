import sys
input = sys.stdin.readline


def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):

    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b


n, m = map(int, input().split())
g = [''] + list(input().split())
parent = list(range(n + 1))
edges = []
res = 0
num = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    c, a, b = edge

    if g[a] == g[b]:
        continue

    if find(a) != find(b):
        res += c
        num += 1
        union(a, b)

if num == n - 1:
    print(res)
else:
    print(-1)
