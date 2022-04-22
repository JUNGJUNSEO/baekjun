import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def lca(u, v):
    while depth[u] != depth[v]:

        if depth[u] > depth[v]:
            u = parent[u]
        else:
            v = parent[v]

    while u != v:
        u = parent[u]
        v = parent[v]

    return u


def dfs(p, d):
    depth[p] = d
    for c in graph[p]:
        if depth[c] < 0:
            parent[c] = p
            dfs(c, d+1)


n = int(input())
graph = [[] for _ in range(n+1)]
depth = [-1]*(n+1)
parent = [0]*(n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1, 0)

m = int(input())

for _ in range(m):
    u, v = map(int, input().split())
    print(lca(u, v))
