from collections import defaultdict

n = int(input())
d_color = defaultdict(int)
balls = []

for idx in range(n):
    c, s = map(int, input().split())
    balls.append((s, c, idx))

balls.sort()
total = 0
ans = [0] * n
j = 0

for i in range(n):

    while balls[i][0] > balls[j][0]:

        total += balls[j][0]
        d_color[balls[j][1]] += balls[j][0]
        j += 1

    ans[balls[i][2]] = total - d_color[balls[i][1]]

for i in range(n):
    print(ans[i])
