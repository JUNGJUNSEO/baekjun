import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if len(graph[k]) == 1:
            print('no')
        else:
            print('yes')
    else:
        print('yes')
