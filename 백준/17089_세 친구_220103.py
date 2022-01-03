def go(index, cnt):
    global ans
    if cnt == 2:
        ans += 1
    for i in range(index, n):
        if index != i and not check[index][i]:
            go(i, cnt + 1)


n, m = map(int, input().split())
check = [[False] * n for _ in range(n)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    check[n1 - 1][n2 - 1] = True
    check[n2 - 1][n1 - 1] = True
for i in range(n):
    print(check[i])
ans = 0
go(0, 0)
print(ans)
