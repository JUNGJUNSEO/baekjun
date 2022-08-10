import sys
input = sys.stdin.readline
# → ↓ ↗ ↘
dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]


def check(x, y, s, idx):
    visit[x][y][i] = True
    cnt = 1

    while True:
        x, y = x+dx[idx], y+dy[idx]
        if 0 <= x < 19 and 0 <= y < 19:
            if a[x][y] == s and not visit[x][y][idx]:
                visit[x][y][idx] = True
                cnt += 1
            else:
                break
        else:
            break
    if cnt == 5:
        return True


a = [list(map(int, input().split())) for _ in range(19)]
visit = [[[False]*4 for _ in range(19)] for _ in range(19)]

for y in range(19):
    for x in range(19):
        for i in range(4):
            if a[x][y] != 0 and not visit[x][y][i]:
                if check(x, y, a[x][y], i):
                    print(a[x][y])
                    print(x+1, y+1)
                    sys.exit()

print(0)
