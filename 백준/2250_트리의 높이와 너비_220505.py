from collections import defaultdict
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def cnt_tree(node):

    if node < 0:
        return 0

    cnt_left, cnt_right = 0, 0

    if tree[node].left > 0:
        cnt_left = cnt_tree(tree[node].left)+1
    if tree[node].right > 0:
        cnt_right = cnt_tree(tree[node].right)+1

    cnt[node] = Node(cnt_left, cnt_right)

    return cnt_left+cnt_right


def solve(level, node, idx):

    if node < 0:
        return

    loc[idx] = level

    left = tree[node].left
    right = tree[node].right

    if left > 0:
        solve(level+1, left, idx-cnt[left].right-1)
    if right > 0:
        solve(level+1, right, idx+cnt[right].left+1)


n = int(input())
tree = dict()
cnt = dict()
loc = [0]*n

for _ in range(n):
    data, left, right = map(int, input().split())
    tree[data] = Node(left, right)

check = [False]*(n+1)

for node in range(1, n+1):
    if tree[node].left > 0:
        check[tree[node].left] = True
    if tree[node].right > 0:
        check[tree[node].right] = True

for i in range(1, n+1):
    if not check[i]:
        root = i
        break
cnt_tree(root)
solve(1, root, cnt[root].left)

d = defaultdict(list)

for i, l in enumerate(loc):
    d[l].append(i)

ans, level = 1, 1
for key in sorted(d.keys()):
    lst = d[key]
    if len(lst) > 1:
        temp = lst[-1]-lst[0]+1
        if temp > ans:
            ans = temp
            level = key
print(level, ans)
