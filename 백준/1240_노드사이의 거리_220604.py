import sys
input = sys.stdin.readline


def solve(idx, res):
    if idx == e:
        print(res)

    check[idx] = True
    for x, d in graph[idx]:
        if not check[x]:
            solve(x, res+d)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    v, u, d = map(int, input().split())
    graph[v].append([u, d])
    graph[u].append([v, d])

for _ in range(m):
    check = [False]*(n+1)
    s, e = map(int, input().split())
    solve(s, 0)
