from collections import deque
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def solve():
    t = 0
    while q:
        x, y, t = q.popleft()

        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if a[nx][ny] != '.' and cnt[nx][ny] >= 0:
                    cnt[nx][ny] += 1
                    if cnt[nx][ny] >= int(a[nx][ny]):
                        cnt[nx][ny] = -1
                        q.append((nx, ny, t+1))
    return t


h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
cnt = [[-1]*w for _ in range(h)]
q = deque()

for x in range(h):
    for y in range(w):
        if a[x][y] != '.':
            cnt[x][y] = 0
            for i in range(8):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if a[nx][ny] == '.':
                        cnt[x][y] += 1
            if cnt[x][y] >= int(a[x][y]):
                cnt[x][y] = -1
                q.append((x, y, 1))

print(solve())
