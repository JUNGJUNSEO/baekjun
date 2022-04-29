def go(x):
    global ans
    if x == n:
        ans += 1
        return
    for y in range(n):
        if not check1[y] and not check2[x+y] and not check3[x-y+n-1]:
            check1[y] = check2[x+y] = check3[x-y+n-1] = True
            go(x+1)
            check1[y] = check2[x+y] = check3[x-y+n-1] = False


n = int(input())

check1 = [False]*n
check2 = [False]*(n*2-1)
check3 = [False]*(n*2-1)
ans = 0
go(0)
print(ans)
