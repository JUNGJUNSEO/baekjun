from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):

    q = deque()
    q.append((0, 0))
    check[0][0] = True
    ans = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if not check[nx][ny]:
                    if a[nx][ny] == '.' or a[nx][ny] == '$' or 'a' <= a[nx][ny] <= 'z':
                        q.append((nx, ny))
                        check[nx][ny] = True

                    if 'a' <= a[nx][ny] <= 'z':
                        k = ord(a[nx][ny])-ord('a')
                        keys[k] = True
                        for ox, oy in doors[k]:
                            check[ox][oy] = True
                            q.append((ox, oy))

                    if 'A' <= a[nx][ny] <= 'Z':
                        k = ord(a[nx][ny])-ord('A')
                        if keys[k]:
                            check[nx][ny] = True
                            q.append((nx, ny))
                        else:
                            doors[k].append((nx, ny))

                    if a[nx][ny] == '$':
                        ans += 1
    return ans


t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    a = [["."]+list(input())+["."] for _ in range(h)]
    a = [["."]*(w+2)] + a + [["."]*(w+2)]
    keys = [False]*26
    for k in list(input()):
        if k != '0':
            keys[ord(k)-ord('a')] = True
    doors = [[] for _ in range(26)]
    check = [[False]*(w+2) for _ in range(h+2)]

    print(bfs(0, 0))
