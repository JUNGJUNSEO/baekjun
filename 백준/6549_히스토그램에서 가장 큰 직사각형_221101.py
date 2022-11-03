while True:

    n, *a = list(map(int, input().split()))

    if n == 0:
        break

    s = []
    ans = 0

    for i in range(n):

        if s and s[-1][0] > a[i]:

            while s and s[-1][0] > a[i]:

                h, idx = s.pop()
                ans = max(ans, (i - idx) * h)

            s.append((a[i], idx))

        else:
            s.append((a[i], i))

    while s:

        h, idx = s.pop()
        ans = max(ans, (n - idx) * h)

    print(ans)
