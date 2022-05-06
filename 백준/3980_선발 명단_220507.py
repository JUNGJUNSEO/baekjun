import sys
input = sys.stdin.readline


def solve(n, s):
    global ans

    if n == 11:
        ans = max(ans, s)
        return

    for i in range(11):
        if a[n][i] > 0 and not check[i]:
            check[i] = True
            solve(n+1, s+a[n][i])
            check[i] = False


t = int(input())
for _ in range(t):
    a = [list(map(int, input().split())) for _ in range(11)]
    check = [False]*11
    ans = 0
    solve(0, 0)
    print(ans)
