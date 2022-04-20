import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solve(lst):

    if not lst:
        return

    root = lst[0]

    idx = 1
    for i in range(1, len(lst)):
        if lst[i] > root:
            idx = i
            break

    if len(lst) > 1:

        solve(lst[1:idx])
        solve(lst[idx:])

    print(root)


tree = list()
try:
    while True:
        tree.append(int(input()))
except:
    solve(tree)
