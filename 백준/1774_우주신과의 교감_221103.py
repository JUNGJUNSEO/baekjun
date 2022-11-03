import math


def get_distance(a, b):

    x1, y1 = nodes[a]
    x2, y2 = nodes[b]

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def find(x):

    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):

    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b


n, m = map(int, input().split())
nodes = []
edges = []
parent = list(range(n+1))
result = 0

for _ in range(n):
    x, y = map(int, input().split())
    nodes.append((x, y))


for i in range(n):
    for j in range(n):
        dist = get_distance(i, j)
        edges.append((dist, i+1, j+1))

edges.sort()

for _ in range(m):

    a, b = map(int, input().split())

    if find(a) != find(b):
        union(a, b)

for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += c

print(format(result, '.2f'))
