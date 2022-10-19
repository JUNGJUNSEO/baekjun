Inf = int(1e9)


def cnt_odd(a):
    cnt = 0
    l = len(a)
    a = int(a)

    for i in range(l-1, -1, -1):
        d = 10**i
        if (a // d) % 2 == 1:
            cnt += 1
        a = a % d
    return cnt


def solve(a, cnt):
    global MIN, MAX
    l = len(a)
    cnt += cnt_odd(a)

    if l == 1:
        MIN = min(MIN, cnt)
        MAX = max(MAX, cnt)
        return

    elif l == 2:
        s = int(a[:1]) + int(a[1:])
        solve(str(s), cnt)

    else:
        for x1 in range(1, l-1):
            for x2 in range(x1+1, l):

                s = int(a[:x1]) + int(a[x1:x2]) + int(a[x2:])

                solve(str(s), cnt)


MIN, MAX = Inf, 0
a = input()
solve(a, 0)

print(MIN, MAX)
