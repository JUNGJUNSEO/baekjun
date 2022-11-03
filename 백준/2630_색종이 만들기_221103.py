def solve(x, y, l):
    global ans_w, ans_b

    cnt_w, cnt_b = 0, 0

    for i in range(x, x+l):
        for j in range(y, y+l):

            if a[i][j] == 0:
                cnt_w += 1
            else:
                cnt_b += 1

    if cnt_w == l*l:
        ans_w += 1
        return
    if cnt_b == l*l:
        ans_b += 1
        return

    for i in range(x, x+l, l//2):
        for j in range(y, y+l, l//2):
            solve(i, j, l//2)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans_w, ans_b = 0, 0
solve(0, 0, n)
print(ans_w)
print(ans_b)
