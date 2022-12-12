from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra_fox():

    q = []
    heappush(q, (0, 1))
    dist_f[1] = 0

    while q:

        cost, node = heappop(q)

        if cost > dist_f[node]:
            continue

        for next in graph[node]:

            if dist_f[next[0]] > cost + next[1]:
                dist_f[next[0]] = cost + next[1]
                heappush(q, (cost + next[1], next[0]))


def dijkstra_wolf():

    q = []
    heappush(q, (0, 1, 0))
    dist_w[1][0] = 0

    while q:

        cost, node, mode = heappop(q)

        if cost > dist_w[node][mode]:
            continue

        for next in graph[node]:

            if mode == 0:
                d = cost + next[1]/2
            else:
                d = cost + next[1]*2

            if dist_w[next[0]][mode ^ 1] > d:
                dist_w[next[0]][mode ^ 1] = d
                heappush(q, (d, next[0], mode ^ 1))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist_f = [INF] * (n + 1)
dist_w = [[INF] * 2 for _ in range(n + 1)]


for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))


dijkstra_fox()
dijkstra_wolf()
print(dist_w)
ans = 0

for i in range(2, n+1):
    if dist_f[i] < min(dist_w[i][0], dist_w[i][1]):
        ans += 1

print(ans)
