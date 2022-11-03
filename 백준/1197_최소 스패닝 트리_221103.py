def find(x):

    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):

    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b


v, e = map(int, input().split())
edges = []
parent = list(range(v+1))
result = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:

    c, a, b = edge

    if find(a) != find(b):
        union(a, b)
        result += c

print(result)
