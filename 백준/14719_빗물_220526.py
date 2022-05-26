h, w = map(int, input().split())
a = [[0]*w for _ in range(h)]
wall = list(map(int, input().split()))

for j in range(w):
    for i in range(wall[j]):
        a[i][j] = 1

ans = 0
for i in range(h):
    check = False
    temp = 0
    for j in range(w):
        if a[i][j] == 1:
            check = True
            if temp > 0:
                ans += temp
                temp = 0
        if check and a[i][j] == 0:
            temp += 1
print(ans)
