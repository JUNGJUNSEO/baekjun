from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(graph, dist):

    q = []
    heappush(q, (0, x))
    dist[x] = 0

    while q:

        cost, node = heappop(q)

        if cost > dist[node]:
            continue

        for next in graph[node]:

            if dist[next[0]] > cost + next[1]:
                dist[next[0]] = cost + next[1]
                heappush(q, (cost + next[1], next[0]))


n, m, x = map(int, input().split())
graph_1 = [[] for _ in range(n + 1)]
graph_2 = [[] for _ in range(n + 1)]
s = [INF] * (n + 1)
e = [INF] * (n + 1)

for _ in range(m):
    a, b, t = map(int, input().split())
    graph_1[a].append((b, t))
    graph_2[b].append((a, t))

dijkstra(graph_2, s)
dijkstra(graph_1, e)

ans = 0

for i in range(1, n+1):

    ans = max(ans, s[i]+e[i])

print(ans)
