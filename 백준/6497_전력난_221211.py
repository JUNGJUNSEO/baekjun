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


while True:

    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    parent = list(range(m))
    edges = []

    for _ in range(n):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()
    ans = 0

    for i in range(n):
        c, a, b = edges[i]

        if find(a) != find(b):
            union(a, b)
        else:
            ans += c

    print(ans)
