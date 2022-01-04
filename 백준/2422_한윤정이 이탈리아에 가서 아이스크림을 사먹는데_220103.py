n, m = map(int, input().split())
check = [[False] * n for _ in range(n)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    check[n1 - 1][n2 - 1] = True
    check[n2 - 1][n1 - 1] = True
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not check[i][j] and not check[j][k] and not check[i][k]:
                ans += 1
print(ans)
