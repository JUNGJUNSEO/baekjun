
a = input()
l = len(a)
ans = ['']*l


def solve(s, e):

    if s == e:
        return

    m = min(a[s:e])
    i = a.index(m)

    ans[i] = a[i]
    print(''.join(ans))
    solve(i+1, e)
    solve(s, i)


solve(0, l)
