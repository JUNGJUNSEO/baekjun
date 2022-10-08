from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
INF = int(1e9)


def get_time(cnt):
    max_time = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                if cnt[i][j] == -1:
                    return -1
                else:
                    max_time = max(cnt[i][j], max_time)

    return max_time


def bfs(case):
    global ans

    cnt = [[-1]*n for _ in range(n)]
    for x, y in case:
        cnt[x][y] = 0
    q = deque(case)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if cnt[nx][ny] >= 0 or a[nx][ny] == 1:
                continue
            cnt[nx][ny] = cnt[x][y] + 1
            q.append((nx, ny))

    time = get_time(cnt)
    if time >= 0:
        ans = min(time, ans)


def get_combinations(idx, cnt):
    if cnt == 0:
        bfs(case)
        return
    for i in range(idx, l):
        case.append(birus[i])
        get_combinations(i+1, cnt-1)
        case.pop()


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
birus = []
ans = INF

for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            birus.append((i, j))

case = []
l = len(birus)
get_combinations(0, m)

print(ans if ans != INF else -1)
