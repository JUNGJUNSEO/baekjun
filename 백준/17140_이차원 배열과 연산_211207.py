from collections import Counter


def go(n, m, a):
    rows = list()
    for row in a:
        row = Counter(row)
        del row[0]
        row = sorted(row.items(), key=lambda x: (x[1], x[0]))
        res = list()
        for element in row:
            res.extend(element)
        m = max(m, len(res))
        if m > 100:
            m = 100
            res = res[0:100]
        rows.append(res)

    a = [[0] * m for _ in range(n)]
    for i in range(n):
        index = 0
        for element in rows[i]:
            a[i][index] = element
            index += 1
    return n, m, a


r, c, k = map(int, input().split())
n, m = 3, 3
a = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for time in range(101):
    if r <= n and c <= m and a[r - 1][c - 1] == k:
        ans = time
        break
    if n >= m:
        n, m, a = go(n, m, a)
    else:
        a = list(zip(*a))
        m, n, a = go(m, n, a)
        a = list(zip(*a))
print(ans)
