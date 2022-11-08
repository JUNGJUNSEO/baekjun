from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def topology_sort():

    q = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            heappush(q, i)

    while q:

        x = heappop(q)
        res.append(x)

        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heappush(q, i)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

res = []
topology_sort()

print(' '.join(map(str, res)))
