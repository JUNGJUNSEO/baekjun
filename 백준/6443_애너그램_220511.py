def solve(s, cnt):
    if cnt == len(a):
        print(s)
        return

    for i in range(len(a)):
        temp = s+a[i]
        if not check[i] and temp not in store:
            store.add(temp)
            check[i] = True
            solve(temp, cnt+1)
            check[i] = False


n = int(input())
for _ in range(n):
    a = list(input())
    store = set()
    a.sort()
    check = [False]*len(a)
    solve('', 0)
