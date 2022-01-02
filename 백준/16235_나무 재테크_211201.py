from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]  # 추가 되는 양분의 양
t = [list(map(int, input().split())) for _ in range(m)]  # tree의 위치와 나이
o = [[5]*n for _ in range(n)]  # 원래 있던 양뷴의 양
tree = [[deque() for _ in range(n)] for _ in range(n)]
for x, y, age in t:
    tree[x-1][y-1].append(age)
for i in range(n):
    for j in range(n):
        sorted(tree[i][j])
for _ in range(k):
    for x in range(n):
        for y in range(n):
            if tree[x][y]:
                # 봄
                die = 0
                for i in range(len(tree[x][y])):
                    age = tree[x][y].popleft()
                    if o[x][y] - age >= 0:
                        o[x][y] -= age
                        tree[x][y].append(age+1)
                    else:
                        die += int(age/2)
                # 여름
                o[x][y] += die
    for x in range(n):
        for y in range(n):
            if tree[x][y]:
                # 가을
                for age in tree[x][y]:
                    if age % 5 == 0:
                        for i in range(8):
                            nx, ny = x+dx[i], y+dy[i]
                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].appendleft(1)
            # 겨울
            o[x][y] += a[x][y]
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)
