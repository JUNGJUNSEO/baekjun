from collections import deque


def dfs(v):
    check[v] = True
    print(v, end=' ')
    for i in a[v]:
        if not check[i]:
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)
    check = [False]*(n+1)
    check[v] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in a[x]:
            if not check[i]:
                check[i] = True
                q.append(i)


n, m, k = map(int, input().split())
a = [[] for _ in range(n+1)]
check = [False]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
for i in range(n+1):
    a[i].sort()
dfs(k)
print()
bfs(k)
