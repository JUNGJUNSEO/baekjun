def raddle():
    check = True
    for i in range(0, 2 * n - 1, 2):
        x, y, visit = 0, i, False
        while x < h:
            if y + 1 < 2 * n - 1 and a[x][y + 1] == 1 and not visit:
                y += 2
                visit = True
                continue
            elif y - 1 >= 0 and a[x][y - 1] == 1 and not visit:
                y -= 2
                visit = True
                continue
            x += 1
            visit = False
        if i != y:
            check = False
            break
    return check


def go(num, index, arr):
    if num == 0:
        return raddle()
    for i in range(index, len(lst)):
        x, y = lst[i]
        if y + 2 < 2 * n - 1 and a[x][y + 2] == 1:
            continue
        if y - 2 >= 0 and a[x][y - 2] == 1:
            continue
        a[x][y] = 1
        if go(num - 1, i + 1, arr + [lst[i]]):
            return True
        a[x][y] = 0


n, m, h = map(int, input().split())
a = [[0] * (2 * n - 1) for _ in range(h)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x - 1][2 * y - 1] = 1  # raddle
lst = list()
for i in range(h):
    for j in range(1, 2 * n - 1, 2):
        if a[i][j] == 0:
            lst.append((i, j))
ans = -1
for i in range(0, 4):
    if go(i, 0, []):
        ans = i
        break
print(ans)
