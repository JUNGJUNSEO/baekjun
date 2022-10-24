from collections import defaultdict


def make_dict(d, p, l):

    for i in range(l):
        s = 0
        for j in range(l - 1):
            s += p[(i + j) % l]
            d[s] += 1

    d[sum(p)] += 1
    d[0] += 1


s = int(input())
n, m = map(int, input().split())
p1, p2 = [], []
for _ in range(n):
    p1.append(int(input()))
for _ in range(m):
    p2.append(int(input()))

d1, d2 = defaultdict(int), defaultdict(int)

make_dict(d1, p1, n)
make_dict(d2, p2, m)

ans = 0

for i in range(s + 1):
    ans += d1[i] * d2[s - i]

print(ans)
