from collections import defaultdict


def disappeare(m):

    for node in tree[m]:
        disappeare(node)

    del tree[m]


n = int(input())
a = list(map(int, input().split()))
m = int(input())
tree = defaultdict(list)
for idx, num in enumerate(a):
    tree[idx]
    if num >= 0:
        tree[num].append(idx)

for value in tree.values():
    if m in value:
        value.remove(m)
disappeare(m)
ans = 0
for value in tree.values():
    if not value:
        ans += 1
print(ans)
