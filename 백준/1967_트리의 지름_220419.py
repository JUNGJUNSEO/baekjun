import sys
sys.setrecursionlimit(10**6)


def solve(parent):
    global ans

    if not tree[parent]:
        return 0

    lst = list()
    for child, weight in tree[parent]:

        lst.append(weight+solve(child))

    lst.sort(reverse=True)
    if len(lst) > 1:
        ans = max(ans, lst[0]+lst[1])
    else:
        ans = max(ans, lst[0])

    return max(lst)


ans = 0
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))

solve(1)
print(ans)
