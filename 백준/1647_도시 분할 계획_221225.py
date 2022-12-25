import sys
input = sys.stdin.readline

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
graph = [[] for _ in range(n + 1)]
parent = list(range(n + 1))
costs = []

for _ in range(m):
    a, b, c = map(int, input().split())
    costs.append((c, a, b))

costs.sort()

ans = 0
max_cost = 0

for c, a, b in costs:
    if find(a) != find(b):
        union(a, b)
        ans += c
        max_cost = max(max_cost, c)

print(ans - max_cost)
