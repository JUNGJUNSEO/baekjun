
def rotate(a):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-1-i] = a[i][j]
    return res


def block_drop(a):
    res = [[0]*n for _ in range(n)]
    for j in range(n):
        tmp = []
        keep_num = 0
        for i in range(n-1, -1, -1):
            if a[i][j] == 0:
                continue

            if not keep_num:
                keep_num = a[i][j]
            else:
                if keep_num == a[i][j]:
                    tmp.append(keep_num*2)
                    keep_num = 0
                else:
                    tmp.append(keep_num)
                    keep_num = a[i][j]
        if keep_num:
            tmp.append(keep_num)

        idx = 0
        for i in range(n-1, -1, -1):
            if idx == len(tmp):
                break
            res[i][j] = tmp[idx]
            idx += 1

    return res


def solve(a, cnt):
    global ans
    if cnt == 0:
        ans = max(ans, max([max(a[i]) for i in range(n)]))
        return

    for _ in range(4):
        drop_a = block_drop(a)
        solve(drop_a, cnt-1)
        a = rotate(a)


ans = 0
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
solve(a, 5)
print(ans)
