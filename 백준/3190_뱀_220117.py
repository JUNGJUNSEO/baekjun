from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move(x, y):
    time = 0
    a[x][y] = 0
    dir = 0  # 오른쪽
    q = deque()
    q.append((x, y))

    while True:
        time += 1
        x, y = x+dx[dir], y+dy[dir]
        if 0 <= x < n and 0 <= y < n and a[x][y]:
            q.append((x, y))
            if a[x][y] == -1:
                rx, ry = q.popleft()
                a[rx][ry] = -1
            a[x][y] = 0
        else:
            return time

        if time in d:
            if d[time] == 'L':
                dir = (dir-1) % 4
            if d[time] == 'D':
                dir = (dir+1) % 4


n = int(input())
k = int(input())
a = [[-1]*n for _ in range(n)]  # -1: 빈칸, 0: 뱀, 1:사과

for _ in range(k):
    ax, ay = map(int, input().split())
    a[ax-1][ay-1] = 1

l = int(input())
d = dict()
for _ in range(l):
    t, dir = input().split()
    d[int(t)] = dir

print(move(0, 0))
