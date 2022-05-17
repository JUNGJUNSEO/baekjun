import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(x):

    if check[x] == 0:
        return x

    if check[x] == 1 or check[x] == 2:
        return -1

    check[x] = 0
    t = dfs(a[x-1])

    if t < 0:
        check[x] = 2
        return -1
    if t != x:
        check[x] = 1
        return t
    if t == x:
        check[x] = 1
        return -1

    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    check = [-1]*(n+1)

    for i in range(1, n+1):
        if check[i] < 0:
            dfs(i)

    ans = 0
    for i in range(1, n+1):
        if check[i] == 2:
            ans += 1
    print(ans)
