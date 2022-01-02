dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
m = int(input())
a = [[0] * n for _ in range(n)]
x, y = int(n // 2), int(n // 2)
a[x][y] = 1
num1, num2 = 1, 1
ax, ay = x + 1, y + 1
while True:
    for i in range(4):
        for _ in range(num1 // 2 + num1 % 2):
            x, y = x + dx[i], y + dy[i]
            num2 += 1
            a[x][y] = num2
            if num2 == m:
                ax, ay = x + 1, y + 1
            if x == 0 and y == 0:
                for i in range(n):
                    print(*a[i])
                print(ax, ay)
                exit()
        num1 += 1
