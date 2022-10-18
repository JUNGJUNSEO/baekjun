from itertools import combinations
Inf = int(1e9)


def mix(case):

    r_sum, g_sum, b_sum = 0, 0, 0
    l = len(case)

    for i in case:
        r, g, b = a[i]
        r_sum += r
        g_sum += g
        b_sum += b

    return r_sum//l, g_sum//l, b_sum//l


n = int(input())
a = []
for _ in range(n):
    r, g, b = map(int, input().split())
    a.append([r, g, b])

r, g, b = map(int, input().split())

ans = Inf
for i in range(2, 8):
    for case in combinations(list(range(n)), i):

        r_sum, g_sum, b_sum = mix(case)

        res = abs(r_sum-r)+abs(g_sum-g)+abs(b_sum-b)
        ans = min(ans, res)

print(ans)
