import sys
input = sys.stdin.readline
n = int(input())
d = dict()
for _ in range(n):
    name, state = input().split()
    d[name] = state
ans = []
for name in d.keys():
    if d[name] == 'enter':
        ans.append(name)
ans = sorted(ans, reverse=True)
for name in ans:
    print(name)
