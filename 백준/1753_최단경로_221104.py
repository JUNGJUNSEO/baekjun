import sys
from heapq import heappop, heappush
input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start):

    distance[start] = 0
    q = []
    heappush(q, (0, start))

    while q:

        dist, node = heappop(q)

        for next in graph[node]:

            cost = next[1] + dist

            if distance[next[0]] > cost:

                distance[next[0]] = cost
                heappush(q, (cost, next[0]))


v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(e + 1)]
distance = [INF] * (e + 1)

for _ in range(e):

    a, b, c = map(int, input().split())

    graph[a].append((b, c))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
