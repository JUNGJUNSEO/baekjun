from collections import deque
import sys
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(x, y, t):
    q = deque()
    q.append((x, y, t))
    cnt[t][x][y] = 0
    while q:
        x, y, t = q.popleft()
        for i in range(4):
            nx, ny = x+mx[i], y+my[i]
            if 0 <= nx < h and 0 <= ny < w:
                if a[nx][ny] == 0 and cnt[t][nx][ny] < 0:
                    cnt[t][nx][ny] = cnt[t][x][y] + 1
                    q.append((nx, ny, t))
        if t+1 <= k:
            for i in range(8):
                nx, ny = x+hx[i], y+hy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if a[nx][ny] == 0 and cnt[t+1][nx][ny] < 0:
                        cnt[t+1][nx][ny] = cnt[t][x][y] + 1
                        q.append((nx, ny, t+1))


k = int(input())
w, h = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
cnt = [[[-1]*w for _ in range(h)] for _ in range(k+1)]
bfs(0, 0, 0)

ans = sys.maxsize
for i in range(k+1):
    if cnt[i][h-1][w-1] >= 0:
        ans = min(ans, cnt[i][h-1][w-1])
print(ans if ans != sys.maxsize else -1)
