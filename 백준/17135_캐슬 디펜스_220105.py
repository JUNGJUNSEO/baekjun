from itertools import combinations
from collections import deque
import copy

dx = [0, -1, 0]
dy = [-1, 0, 1]


def bfs(x, y):

    dis[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()

        if dis[x][y] <= d:
            if a1[x][y] == 1:
                die.append((x, y))
                return
        else:
            return

        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not dis[nx][ny]:
                    dis[nx][ny] = dis[x][y] + 1
                    q.append((nx, ny))


n, m, d = map(int, input().split())
a0 = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for option in combinations(range(m), 3):
    a1 = copy.deepcopy(a0)
    res = 0
    for i in range(n):
        die = list()
        for j in option:
            dis = [[0] * m for _ in range(n - i)]
            bfs(n - (i + 1), j)
        for x, y in set(die):
            a1[x][y] = 0
            res += 1
    ans = max(ans, res)
print(ans)
