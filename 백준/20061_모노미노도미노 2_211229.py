from collections import deque


def remove_block(a):
    global score

    # 진한색 일 떄
    for i in range(6, 10):
        line = True
        for j in range(4):
            if a[i][j] == 0:
                line = False
                break
        # 줄 삭제
        if line:
            score += 1
            del a[i]
            a.appendleft([0]*4)

    # 연한색 일 때
    for i in range(4, 6):
        for j in range(4):
            # 줄 삭제
            if a[i][j] == 1:
                del a[9]
                a.appendleft([0]*4)
                break


def move_block(a, block, t):

    mx, my = 10, 10
    for nx, ny in block:
        while True:
            nx += 1
            if not(0 <= nx < 10) or a[nx][ny]:
                mx, my = min(mx, nx-1), min(my, ny)
                break

    a[mx][my] = 1
    if t == 2:
        a[mx][my+1] = 1
    if t == 3:
        a[mx-1][my] = 1


green = deque([[0] * 4 for _ in range(10)])
blue = deque([[0] * 4 for _ in range(10)])
n = int(input())
score = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    block = list()

    block.append((x, y))
    if t == 2:
        block.append((x, y+1))
    if t == 3:
        block.append((x+1, y))

    # 시계 방향으로 회전
    block_rotate = list()
    for x, y in block:
        x, y = y, 4-1-x
        block_rotate.append((x, y))

    move_block(green, block, t)
    move_block(blue, block_rotate, t ^ 1)

    remove_block(green)
    remove_block(blue)


print(score)
print(sum(sum(blue[i])+sum(green[i])for i in range(10)))
