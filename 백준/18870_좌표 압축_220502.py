import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = dict()

for i, e in enumerate(sorted(list(set(a)))):
    d[e] = i

for e in a:
    print(d[e], end=' ')
