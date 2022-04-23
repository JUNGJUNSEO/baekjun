import sys
input = sys.stdin.readline


def getParent():
    idx = -1
    parent[a[0]] = -1

    for i in range(n-1):
        if a[i+1] != a[i]+1:
            idx += 1

        parent[a[i+1]] = a[idx]


def solve():
    ans = 0

    for node in a[1:]:
        if parent[node] != parent[k] and parent[parent[node]] == parent[parent[k]]:
            ans += 1

    return ans


while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    a = list(map(int, input().split()))
    parent = dict()

    getParent()
    print(solve())
