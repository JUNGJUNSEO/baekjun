import sys
import copy
from itertools import permutations

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate(x, y, s):
    if s == 0:
        return
    for i in range(4):
        for _ in range(s * 2):
            ox, oy = x, y
            x, y = x + dx[i], y + dy[i]
            a2[x][y] = a1[ox][oy]
    rotate(x + 1, y + 1, s - 1)


n, m, k = map(int, input().split())
a0 = [list(map(int, input().split())) for _ in range(n)]
info = [list(map(int, input().split())) for _ in range(k)]
ans = sys.maxsize
for order in permutations(info, k):
    a1 = copy.deepcopy(a0)
    for r, c, s in order:
        a2 = copy.deepcopy(a1)
        rotate(r - (s + 1), c - (s + 1), s)
        a1 = a2
    for row in range(n):
        ans = min(ans, sum(a1[row]))
print(ans)
