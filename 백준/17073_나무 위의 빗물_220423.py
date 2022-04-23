from collections import deque
import sys
input = sys.stdin.readline


def bfs(x):
    visit[x] = True
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visit[nx]:
                tree[x].append(nx)
                q.append(nx)
                visit[nx] = True


n, w = map(int, input().split())
graph = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
visit = [False]*(n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(1)
cnt = 0

for i in range(1, n+1):
    if not tree[i]:
        cnt += 1

print(w/cnt)
