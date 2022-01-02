dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
ans, num1, num2 = 0, True, True
while True:

    if num1:
        ans += 1
        cnt = 0
        check[r][c] = True

    if num2:
        nx, ny = r+dx[((d-1)+4) % 4], c+dy[((d-1)+4) % 4]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and not check[nx][ny]:
                r, c = nx, ny
                num1, num2 = True, True
            else:
                cnt += 1
                num1, num2 = False, True
            d = ((d-1)+4) % 4
    if cnt == 4:
        r, c = r+dx[(d+2) % 4], c+dy[(d+2) % 4]
        if 0 <= r < n and 0 <= c < m and a[r][c] == 0:
            num1, num2, cnt = False, True, 0
        else:
            break
print(ans)
