dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def possible(x, y, size):

    for i in range(4):
        for l in range(size+1):
            nx, ny = x+dx[i]*l, y+dy[i]*l
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == "." or check[nx][ny]:
                    return False
            else:
                return False
    return True


def cover(x, y, size, bool):

    for i in range(4):
        for l in range(size+1):
            nx, ny = x+dx[i]*l, y+dy[i]*l
            check[nx][ny] = bool


def solve(cnt, num, res):
    global ans

    if cnt == 2:
        ans = max(ans, res)
        return
    if num == n*m:
        return

    x, y = num//m, num % m

    if a[x][y] == "#" and not check[x][y]:
        for size in range(n*m//2):
            if possible(x, y, size):
                cover(x, y, size, True)
                solve(cnt+1, num+1, res*(size*4+1))
                cover(x, y, size, False)

    solve(cnt, num+1, res)


n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
check = [[False]*m for _ in range(n)]
ans = 0
solve(0, 0, 1)
print(ans)
