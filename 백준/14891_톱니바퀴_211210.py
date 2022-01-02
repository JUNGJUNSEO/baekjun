from collections import deque


def go(x, m, num1, num2):
    if 1 <= x <= 4 and not check[x-1]:
        if a[n-1][num1] != a[x-1][num2]:
            rotate[x-1] = -m
            q.append((x, -m))
            check[x-1] = True


a = [deque(map(int, input())) for _ in range(4)]
for _ in range(int(input())):
    n, m = map(int, input().split())
    rotate = [0]*4
    check = [False]*4
    rotate[n-1] = m
    check[n-1] = True
    q = deque()
    q.append((n, m))
    while q:
        n, m = q.popleft()
        go(n+1, m, 2, 6)
        go(n-1, m, 6, 2)
    for index, d in enumerate(rotate):
        a[index].rotate(d)
score = 0
for i in range(4):
    if a[i][0] == 1:
        score += 2**i
print(score)
