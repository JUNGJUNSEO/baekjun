import sys
from collections import deque
input = sys.stdin.readline


def topology_sort():

    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:

        x = q.popleft()

        for nx in graph[x]:

            indegree[nx] -= 1
            res[nx] = max(res[nx], d[nx-1]+res[x])

            if indegree[nx] == 0:
                q.append(nx)


t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    res = [0] * (n + 1)

    for _ in range(k):

        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    for i in range(1, n + 1):
        res[i] = d[i-1]

    topology_sort()

    w = int(input())

    print(res[w])
