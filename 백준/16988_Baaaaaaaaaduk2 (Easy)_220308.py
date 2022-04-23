from itertools import combinations
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visit):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    cnt = 1
    catch = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 2 and not visit[nx][ny]:
                    q.append((nx, ny))
                    visit[nx][ny] = True
                    cnt += 1
                if a[nx][ny] == 0:
                    catch = False
    if catch:
        return cnt
    else:
        return 0


def solve(case):

    for x, y in case:
        a[x][y] = 1
    visit = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2 and not visit[i][j]:
                cnt += bfs(i, j, visit)

    for x, y in case:
        a[x][y] = 0
    return cnt


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
zeros = list()
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            zeros.append((i, j))
ans = 0
for case in combinations(zeros, 2):
    ans = max(ans, solve(case))
print(ans)
