import sys
import copy
from itertools import permutations

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 회전
def rotate(x, y, s):
    if s == 0:
        return
    temp = a1[x][y]
    for dir in range(4):
        for _ in range(s * 2):
            x, y = x + dx[dir], y + dy[dir]
            temp, a1[x][y] = a1[x][y], temp
    rotate(x + 1, y + 1, s - 1)


n, m, k = map(int, input().split())
a0 = [list(map(int, input().split())) for _ in range(n)]
info = [list(map(int, input().split())) for _ in range(k)]
ans = sys.maxsize

for option in permutations(info, k):
    a1 = copy.deepcopy(a0)
    for r, c, s in option:
        rotate(r - (s + 1), c - (s + 1), s)
    for row in range(n):
        ans = min(ans, sum(a1[row]))
print(ans)
