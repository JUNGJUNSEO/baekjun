import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def find():
    lst = list()
    for num in range(n*n):
        x, y = num // n, num % n

        if a[x][y] == 0:
            cnt_f, cnt_e = 0, 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] in f:
                        cnt_f += 1
                    if a[nx][ny] == 0:
                        cnt_e += 1
            lst.append([cnt_f, cnt_e, num])

    lst = sorted(lst, key=lambda x: (-x[0], -x[1], x[2]))
    a[lst[0][2]//n][lst[0][2] % n] = s


n = int(input())
a = [[0]*n for _ in range(n)]
like = [{} for _ in range(n*n)]

for _ in range(n*n):
    s, *f = map(int, input().split())
    f = set(f)
    find()
    like[s-1] = f

ans = 0

for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] in like[a[x][y]-1]:
                    cnt += 1
        if cnt == 4:
            ans += 1000
        elif cnt == 3:
            ans += 100
        elif cnt == 2:
            ans += 10
        elif cnt == 1:
            ans += 1
print(ans)
