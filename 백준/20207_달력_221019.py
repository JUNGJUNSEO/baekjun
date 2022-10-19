def bfs(x):

    for i in range(1, l):
        visit[i] = False

    visit[x] = True
    q = []
    q.append(x)

    while q:
        x = q.pop()
        x = x+1
        if x < l:
            if c[x] > 0 and not visit[x]:
                visit[x] = True
                q.append(x)


def get_area():

    cnt = 0
    h = 0

    for i in range(1, l):
        if visit[i]:
            cnt += 1
            h = max(h, c[i])

    return cnt*h


n = int(input())
l = 365 + 1
c = [0]*l
visit = [False]*l

for _ in range(n):
    x1, x2 = map(int, input().split())

    for x in range(x1, x2+1):
        c[x] += 1
ans = 0

for i in range(1, l):
    if c[i] > 0 and not visit[i]:
        bfs(i)
        ans += get_area()

print(ans)
