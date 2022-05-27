n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def solve(n, a):

    if n == 0:
        return a[0][0]

    b = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            lst = list()
            for nx in range(x*2, x*2+2):
                for ny in range(y*2, y*2+2):
                    lst.append(a[nx][ny])

            b[x][y] = sorted(lst)[-2]

    return solve(n//2, b)


print(solve(n//2, a))
