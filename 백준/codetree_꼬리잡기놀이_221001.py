from collections import deque
import copy
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def dfs(x, y, cnt):
    if a[x][y] != 4:
        t_que[num].append(cnt+1)
    else:
        t_que[num].append(-1)
    team[x][y] = num
    path[x][y] = cnt
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] > 0 and path[nx][ny] < 0:
                dfs(nx, ny, cnt+1)


def get_round():

    for i in range(n):
        round.append((i, 0, 0))
    for j in range(n):
        round.append((n-1, j, 1))
    for i in range(n-1, -1, -1):
        round.append((i, n-1, 2))
    for j in range(n-1, -1, -1):
        round.append((0, j, 3))


def move():
    for i in range(m):
        if not reverse[i]:
            t_que[i].rotate(-1)
            r_que[i].rotate(-1)
        else:
            t_que[i].rotate(1)
            r_que[i].rotate(1)


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
path = [[-1]*n for _ in range(n)]
team = [[-1]*n for _ in range(n)]
t_que = [deque() for _ in range(m)]
reverse = [False]*m
round = []
get_round()
num = 0

for x in range(n):
    for y in range(n):
        if a[x][y] == 1:
            t_que[num].append(1)
            team[x][y] = num
            path[x][y] = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] == 2:
                        if x-nx > 0 or y-ny > 0:
                            dir[num] = 0
                        if x-nx < 0 or y-ny < 0:
                            dir[num] = 1
                        dfs(nx, ny, 1)
                        num += 1
                        break

r_que = [deque() for _ in range(m)]
for i in range(m):
    q = t_que[i]
    q_max = max(q)
    for c in q:
        if c > 0:
            r_que[i].append(q_max+1-c)
        else:
            r_que[i].append(c)


ans = 0
for i in range(k):
    i = i % (n*4)
    move()
    x, y, d = round[i]
    for _ in range(n):
        if team[x][y] >= 0:
            if not reverse[team[x][y]]:
                if t_que[team[x][y]][path[x][y]] > 0:
                    ans += t_que[team[x][y]][path[x][y]]**2
                    reverse[team[x][y]] = True
                    break
            else:
                if r_que[team[x][y]][path[x][y]] > 0:
                    ans += r_que[team[x][y]][path[x][y]]**2
                    reverse[team[x][y]] = False
                    break

        x, y = x+dx[d], y+dy[d]
print(ans)
