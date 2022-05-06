dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n = int(input())
a = [[-1]*(n) for _ in range(n)]
d = dict()
order = list()
for _ in range(n**2):
    num, *like = map(int, input().split())
    order.append(num)
    d[num] = like

for num in order:

    max_like, max_empty, mx, my = -1, -1, 0, 0

    for x in range(n):
        for y in range(n):
            if a[x][y] >= 0:
                continue

            like, empty = 0, 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] in d[num]:
                        like += 1
                    if a[nx][ny] < 0:
                        empty += 1

            if like > max_like or (like == max_like and empty > max_empty):
                max_like = like
                max_empty = empty
                mx, my = x, y

    a[mx][my] = num

ans = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] in d[a[x][y]]:
                    cnt += 1
        if cnt > 0:
            ans += 10**(cnt-1)
print(ans)
