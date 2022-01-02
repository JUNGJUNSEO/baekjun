dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n = int(input())
student = [[False] * (n ** 2) for _ in range(n ** 2)]
for _ in range(n ** 2):
    num, *love = list(map(int, input().split()))
    for i in love:
        student[num - 1][i - 1] = True


a[x][y] = num
