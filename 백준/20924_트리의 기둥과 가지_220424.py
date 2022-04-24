import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(p):
    visit[p] = True

    for c, l in graph[p]:
        if not visit[c]:
            tree[p].append((c, l))
            dfs(c)


def solve(p, length):
    global pole, check

    if check and len(tree[p]) != 1:
        pole, check = length, False

    if not tree[p]:
        return length

    total = 0
    for c, l in tree[p]:
        total = max(total, solve(c, length+l))
    return total


n, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
tree = [[] for _ in range(n+1)]
pole, check = 0, True

for _ in range(n-1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

dfs(r)

branch = solve(r, 0)
print(pole, branch-pole)
