def dfs(x, index):
    if index == n:
        return
    check[x] = True
    for _ in range(len(a[x])):
        if not check[l[index+1]]:
            dfs(l[index+1], index+1)


n = int(input())
a = [[]for _ in range(n+1)]
check = [False]*(n+1)
for _ in range(n-1):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
l = list(map(int, input().split()))
dfs(l[0], 0)
print(check)
