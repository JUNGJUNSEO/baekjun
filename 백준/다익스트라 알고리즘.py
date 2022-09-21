import heapq
INF = int(1e9)

# n: 노드의 개수, m: 간선의 개수
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        for node, cost in graph[now]:
            dist = distance[now]+cost
            if distance[node] > dist:
                distance[node] = dist
                heapq.heappush(q, (dist, node))


# 1번 노드에서 출발
dijkstra(1)

for i in range(1, n+1):
    if distance[i] == INF:
        print('도달할 수 없습니다.')
    else:
        print(distance[i])
