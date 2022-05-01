import sys


def possible(x, y, l):
    for i in range(x, x+l):
        for j in range(y, y+l):
            if not (0 <= i < 10 and 0 <= j < 10):
                return False
            if a[i][j] == 0 or cover[i][j]:
                return False
    return True


def check(x, y, l, bool):
    for i in range(x, x+l):
        for j in range(y, y+l):
            cover[i][j] = bool


def solve(index, res):
    global ans
    if index == 100:
        ans = min(ans, res)
        return

    x, y = index//10, index % 10
    if a[x][y] == 1 and not cover[x][y]:
        for k in range(5):
            if possible(x, y, k+1) and cnt[k] < 5:
                check(x, y, k+1, True)
                cnt[k] += 1
                solve(index+1, res+1)
                cnt[k] -= 1
                check(x, y, k+1, False)
    else:
        solve(index+1, res)


a = [list(map(int, input().split())) for _ in range(10)]
cover = [[False]*10 for _ in range(10)]
cnt = [0]*5
ans = sys.maxsize
solve(0, 0)
print(ans) if ans != sys.maxsize else print(-1)
