def solve(w, c):
    global ans

    if w < 500:
        return

    if c == n:
        ans += 1
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            solve(w - k + a[i], c + 1)
            check[i] = False


n, k = map(int, input().split())
check = [False]*n
a = list(map(int, input().split()))
ans = 0
solve(500, 0)
print(ans)
