import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve(num, x, y, cnt):
    while True:
        for i in range(4):
            for _ in range(num//2+num % 2):
                x, y = x+dx[i], y+dy[i]
                a[x][y] = cnt
                if cnt == m:
                    ax, ay = x+1, y+1
                cnt += 1

                if x == 0 and y == 0:
                    for i in range(n):
                        print(' '.join(map(str, a[i])))
                    print(ax, ay)
                    return
            num += 1


n = int(input())
m = int(input())
a = [[0]*n for _ in range(n)]
num = 1
x, y = n//2, n//2
a[x][y] = 1
cnt = 2
solve(num, x, y, cnt)
