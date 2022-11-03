from collections import deque

n, k = map(int, input().split())
d = list(map(int, input().split()))
r = [False]*2*n
d = deque(d)
r = deque(r)
ans = 0

while True:
    ans += 1
    # 1
    d.rotate(1)
    r.rotate(1)
    r[n-1] = False
    # 2
    for i in range(n-1, -1, -1):
        if r[i] and d[i+1] > 0 and not r[i+1]:
            d[i+1] -= 1
            r[i], r[i+1] = False, True
            if d[i+1] == 0:
                k -= 1
            # 로봇 하차
            if i+1 == n-1:
                r[i+1] = False

    # 3
    if d[0] > 0 and not r[0]:
        d[0] -= 1
        r[0] = True
        if d[0] == 0:
            k -= 1

    if k <= 0:
        print(ans)
        break
