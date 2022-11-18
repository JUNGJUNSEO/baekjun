from heapq import heappop, heappush
INF = int(1e9)


def dijkstra(num):

    dist = [INF] * (n+1)
    dist[num] = 0
    q = []
    heappush(q, (0, num))

    while q:

        cost, node = heappop(q)

        if dist[node] < cost:
            continue

        for next_node, distance in graph[node]:

            next_cost = cost + distance

            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                parent[num][next_node] = node
                heappush(q, (next_cost, next_node))


def get_parent(num, idx):

    if num == idx:
        return 0

    if idx != parent[num][idx]:
        p = get_parent(num, parent[num][idx])

        if p == 0:
            parent[num][idx] = idx
        else:
            parent[num][idx] = p

    return parent[num][idx]


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = [['-'] * (n+1) for _ in range(n+1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


for i in range(1, n+1):
    dijkstra(i)

for i in range(1, n+1):
    for j in range(1, n+1):
        get_parent(i, j)

for i in range(1, n+1):
    print(' '.join(map(str, parent[i][1:])))
