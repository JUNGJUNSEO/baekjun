dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

blocks = {'|': [2, 3], '-': [0, 1], '+': [0, 1, 2, 3],
          '1': [0, 2], '2': [0, 3], '3': [1, 3], '4': [1, 2]}


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
check = [[False]*c for _ in range(r)]
cnt = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if a[i][j] == '.':
            continue
        if a[i][j] == 'M' or a[i][j] == 'Z':
            cnt[i][j] = 1
        elif a[i][j] == '+':
            cnt[i][j] = 4
        else:
            cnt[i][j] = 2


for x in range(r):
    for y in range(c):

        if a[x][y] == '.':
            continue
        if a[x][y] == 'M' or a[x][y] == 'Z':

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not in_range(nx, ny):
                    continue
                if a[nx][ny] == '.':
                    continue
                cnt[nx][ny] -= 1

            continue

        for i in blocks[a[x][y]]:
            nx, ny = x + dx[i], y + dy[i]

            cnt[nx][ny] -= 1


for x in range(r):
    for y in range(c):
        if cnt[x][y] < 0:

            for block, dir in blocks.items():

                total = abs(cnt[x][y])
                check = True

                for i in dir:
                    nx, ny = x + dx[i], y + dy[i]

                    if not in_range(nx, ny):
                        check = False
                        break
                    if cnt[nx][ny] == 1:
                        total -= 1
                    if cnt[nx][ny] == 0:
                        check = False
                        break

                if check and total == 0:
                    print(x+1, y+1, block)
                    exit()
