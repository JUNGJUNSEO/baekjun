from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def destroy(x, y, d, s):
    for _ in range(s):
        x, y = x+dx[d-1], y+dy[d-1]
        a[x][y] = 0


def move(x, y):
    l = 1
    lst = list()
    while True:
        for i in [2, 1, 3, 0]:
            for _ in range(l//2 + l % 2):
                x, y = x+dx[i], y+dy[i]
                if a[x][y]:
                    lst.append(a[x][y])
                if x == 0 and y == 0:
                    return lst
            l += 1


def explosion(lst):
    
    cnt = 1
    start = lst[0]
    temp = list()
    result = list()

    for elem in range(lst):
        if start == elem:
            temp.append
        else:
            result += [cnt, start]
            cnt = 1
            start = elem
            
    return result


def duplicate(lst):
    
    cnt = 1
    start = lst[0]
    result = list()

    for elem in range(lst):
        if start == elem:
            cnt += 1
        else:
            result += [cnt, start]
            cnt = 1
            start = elem
            
    return result

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
sx, sy = (n+1)//2-1, (n+1)//2-1
marble = [0]*4

for _ in range(m):
    d, s = map(int, input().split())
    destroy(sx, sy, d, s)
    check = True
    while check:
        if q:
            a = move(sx, sy)
            check = explosion(sx, sy)
        else:
            check = False

    q = duplicate(sx, sy)
    if q:
        a = move(sx, sy)
ans = 0
for idx, num in enumerate(marble):
    ans += idx*num
print(ans)
