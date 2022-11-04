def find(x):

    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):

    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b


n = int(input())
c = []

for i in range(n):
    x, y, z = map(int, input().split())
    c.append((x, y, z, i))

parent = list(range(n))
result = 0
edges = []

for i in range(3):
    s = sorted(c, key=lambda x: x[i])

    for j in range(n-1):
        edges.append((abs(s[j][i] - s[j+1][i]), s[j][3], s[j+1][3]))


edges.sort()

for c, a, b in edges:

    if find(a) != find(b):
        union(a, b)
        result += c

print(result)
