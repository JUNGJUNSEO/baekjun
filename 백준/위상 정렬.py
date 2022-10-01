from collections import deque


def topology_sort():
    q = deque()
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


v, e = map(int, input().split())
indegree = [0]*v
graph = [[] for _ in range(v)]
result = list()
for _ in range(e):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1
topology_sort()
print(result)
