import sys
sys.setrecursionlimit(10**6)


def solve(name):

    fold = []

    if name not in doc:
        cnt[name] = [0, 0]
        return fold

    for f in doc[name]:
        n, s = f

        if s == '0':
            fold.append(n)
        else:
            fold = solve(n) + fold

    cnt[name] = [len(set(fold)), len(fold)]

    return fold


doc = {}
cnt = {}

n, m = map(int, input().split())

for _ in range(n + m):
    upper, lower, s = input().split()

    if upper in doc:
        doc[upper].append([lower, s])
    else:
        doc[upper] = []
        doc[upper].append([lower, s])

solve('main')

q = int(input())
for _ in range(q):
    path = input().split('/')
    c1, c2 = cnt[path[-1]]
    print(c1, c2)
