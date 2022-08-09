from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dir = {2: [2, 0, 3, 1], 0: [0, 3, 1, 2], 3: [3, 1, 2, 0], 1: [1, 2, 0, 3]}


def order(x, y, d, cnt, q):
    # 명령 2
    lst = dir[d]
    for idx, nd in enumerate(lst[:3]):
        q.append((x, y, nd, cnt+idx))
    q.append((x, y, lst[-1], cnt+1))


def bfs(x, y, d, cnt):
    q = deque()
    order(x, y, d, cnt, q)
    visit[x][y] = True

    while q:
        x, y, d, cnt = q.popleft()
        if x == ex-1 and y == ey-1 and d == ed-1:
            print(cnt)

        # 명령 1
        for i in range(1, 4):
            nx, ny = x+dx[d]*i, y+dy[d]*i
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0:
                    if not visit[nx][ny]:
                        visit[nx][ny] = True
                        order(nx, ny, d, cnt+1, q)
                else:
                    break


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())

bfs(sx-1, sy-1, sd-1, 0)
