from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 부분 행렬을 시계 방향으로 90도 회전


def rotate(l):
    l = 2**l
    result = [[0]*n for _ in range(n)]

    for x in range(n//l):
        for y in range(n//l):

            for i in range(x, x+l):
                for j in range(y, y+l):
                    result[(x-y)+j][(x+y)+l-1-i] = a[i][j]

    return result

# 얼음 줄어 듬


def remove(a):
    lst = list()
    for x in range(n):
        for y in range(n):
            cnt = 0
            if not a[x][y]:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < n and a[nx][ny]:
                    cnt += 1
            if cnt < 3:
                lst.append((x, y))
    for x, y in lst:
        a[x][y] -= 1

# 얼음 덩어리 구하기


def bfs(x, y):
    q = deque()
    q.append((x, y))
    check[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not check[nx][ny] and a[nx][ny]:
                    check[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1

    return cnt


n, q = map(int, input().split())
n = 2**n
a = [list(map(int, input().split())) for _ in range(n)]
length = list(map(int, input().split()))

for l in length:
    a = remove(rotate(l))

check = [[False]*n for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if not check[i][j] and a[i][j]:
            cnt = max(bfs(i, j), cnt)

print(sum(sum(a[i]) for i in range(n)))
print(cnt)
