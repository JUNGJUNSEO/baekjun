from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def shark1(num, x, y):
    global cnt
    for d in pri[num][dir[num] - 1]:  # [1,2,3,4]
        nx, ny = x + dx[d - 1], y + dy[d - 1]
        if 0 <= nx < n and 0 <= ny < n:
            if not trace_a[nx][ny]:
                if a[nx][ny]:
                    shark_loc[num] = []
                    a[x][y] = 0
                    cnt -= 1
                else:
                    a[x][y], a[nx][ny] = 0, num + 1
                    shark_loc[num] = [nx, ny]
                dir[num] = d
                return True


def shark2(num, x, y, c):
    for d in pri[num][dir[num] - 1]:  # [1,2,3,4]
        nx, ny = x + dx[d - 1], y + dy[d - 1]
        if 0 <= nx < n and 0 <= ny < n:
            if c in trace_a[nx][ny]:
                a[x][y], a[nx][ny] = 0, num + 1
                shark_loc[num] = [nx, ny]
                dir[num] = d
                return True


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dir = list(map(int, input().split()))
shark_loc = [[] for _ in range(m)]
for i in range(n):
    for j in range(n):
        if a[i][j]:
            shark_loc[a[i][j] - 1] = [i, j]
pri = [[] for _ in range(m)]
for i in range(m):
    pri[i] = [list(map(int, input().split())) for _ in range(4)]
trace = [deque() for _ in range(m)]
trace_a = [[list() for _ in range(n)] for _ in range(n)]
ans, cnt = 0, m
while ans < 1000:
    for i in range(m):
        if not shark_loc[i]:
            continue
        x, y = shark_loc[i]
        trace[i].append((x, y))
        trace_a[x][y].append(i + 1)

    for i in range(m):
        if not shark_loc[i]:
            continue
        x, y = shark_loc[i]
        if shark1(i, x, y):
            continue
        shark2(i, x, y, i + 1)

    if len(trace[0]) == k:
        for i in range(m):
            if trace[i]:
                sx, sy = trace[i].popleft()
                trace_a[sx][sy].pop()
    ans += 1
    if cnt == 1:
        print(ans)
        exit()
print(-1)
