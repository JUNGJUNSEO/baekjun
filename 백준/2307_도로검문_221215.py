import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = int(1e9)


def dijkstra():

    dist = [INF] * (n + 1)
    q = []
    heappush(q, (0, 1))
    dist[1] = 0

    while q:

        cost, node = heappop(q)

        if cost > dist[node]:
            continue

        for next_node, next_cost in graph[node]:

            if dist[next_node] > cost + next_cost:
                dist[next_node] = cost + next_cost
                parent[next_node] = node

                heappush(q, (cost + next_cost, next_node))

    return dist[n]


def dijkstra_police(police_node):

    dist = [INF] * (n + 1)
    q = []
    heappush(q, (0, 1))
    dist[1] = 0

    while q:

        cost, node = heappop(q)

        if cost > dist[node]:
            continue

        for next_node, next_cost in graph[node]:

            if next_node == police_node:
                continue

            if dist[next_node] > cost + next_cost:
                dist[next_node] = cost + next_cost

                heappush(q, (cost + next_cost, next_node))

    return dist[n]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
parent = list(range(n + 1))

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

dist_t = dijkstra()

node = n
ans = 0

while True:

    node = parent[node]

    if node == 1:
        break

    dist_p = dijkstra_police(node)

    if dist_p == INF:
        ans = -1
        break

    ans = max(ans, dist_p - dist_t)

print(ans)
