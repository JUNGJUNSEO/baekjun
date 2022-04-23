from itertools import product, permutations
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def clock(a):
    result = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            result[j][4-i] = a[i][j]
    return result


def bfs(case):
    global ans

    cube = list()
    for idx, elem in enumerate(case):
        cube.append(cubes[idx][elem])
    for arr in permutations(cube):
        if arr[0][0][0] == 0 or arr[4][4][4] == 0:
            continue
        dist = [[[-1]*5 for _ in range(5)] for _ in range(5)]
        dist[0][0][0] = 0
        q = deque()
        q.append((0, 0, 0))
        while q:
            z, x, y = q.popleft()
            if z == 4 and x == 4 and y == 4:
                ans = min(ans, dist[4][x][y])
                if ans == 12:
                    print(ans)
                    exit()
                break
            for i in range(6):
                nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                    if dist[nz][nx][ny] < 0 and arr[nz][nx][ny] == 1:
                        dist[nz][nx][ny] = dist[z][x][y]+1
                        q.append((nz, nx, ny))


cubes = list()
for _ in range(5):
    rotates = list()
    a = [list(map(int, input().split())) for _ in range(5)]
    for _ in range(4):
        a = clock(a)
        rotates.append(a)
    cubes.append(rotates)
ans = sys.maxsize
for case in product(range(4), repeat=5):
    bfs(case)
print(ans if ans != sys.maxsize else -1)
