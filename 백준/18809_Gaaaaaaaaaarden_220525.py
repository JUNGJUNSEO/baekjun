import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solve():
    res = 0
    board = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    q = deque()

    for x, y in case1:
        if [x, y] in case2:
            board[x][y][0] = 0
        else:
            board[x][y][0] = 1
        board[x][y][1] = 0
        q.append((x, y))

    while q:
        # 0:green, 1:red, 2:flower
        x, y = q.popleft()
        if board[x][y][0] == 2:
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] > 0:
                if board[nx][ny][0] < 0:
                    board[nx][ny][0] = board[x][y][0]
                    board[nx][ny][1] = board[x][y][1]+1
                    q.append((nx, ny))
                elif board[nx][ny][0] == 0 or board[nx][ny][0] == 1:
                    if board[nx][ny][0] != board[x][y][0] and board[nx][ny][1] == board[x][y][1]+1:
                        board[nx][ny][0] = 2
                        res += 1
    return res


n, m, g, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
lst = list()

for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            lst.append([i, j])
ans = 0
for case1 in combinations(lst, g+r):
    for case2 in combinations(case1, g):
        ans = max(ans, solve())
print(ans)
