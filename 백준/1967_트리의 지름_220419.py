import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solve(parent):
    global ans

    w1, w2 = 0, 0
    for child, weight in sorted(tree[parent], key=lambda x: -x[1]):

        temp = weight+solve(child)

        if temp > w1:
            w1 = temp
        else:
            w2 = max(w2, temp)

    ans = max(ans, w1+w2)

    return w1


ans = 0
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))

solve(1)
print(ans)
