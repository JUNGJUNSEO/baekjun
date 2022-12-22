import copy
import sys
input = sys.stdin.readline


def solve():

    for k in range(n):
        for i in range(n):
            for j in range(n):

                if i == j or i == k or k == j:
                    continue

                if a[i][j] == a[i][k] + a[k][j]:
                    dist[i][j] = 0
                elif a[i][j] > a[i][k] + a[k][j]:
                    return -1

    return sum([sum(dist[i]) for i in range(n)]) // 2


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dist = copy.deepcopy(a)
print(solve())
