import sys
input = sys.stdin.readline


def dfs(parent, total):

    dist[parent] = total

    for child, weight in graph[parent]:
        if dist[child] < 0:
            dfs(child, total+weight)


n = int(input())
graph = [[] for _ in range(n+1)]
dist = [-1]*(n+1)

for _ in range(n):

    a, *b = map(int, input().split())
    b = b[:-1]

    for i in range(0, len(b), 2):
        graph[a].append((b[i], b[i+1]))

dfs(1, 0)
idx = dist.index(max(dist))
dist = [-1]*(n+1)
dfs(idx, 0)
print(max(dist))
