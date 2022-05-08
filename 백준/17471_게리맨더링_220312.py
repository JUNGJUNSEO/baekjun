from itertools import combinations
import sys


def connect(index, bool):
    visit[index] = True
    if bool:
        arr1.append(index)
    else:
        arr2.append(index)
    for i in b[index]:
        if bool:
            if check[i-1] and not visit[i-1]:
                connect(i-1, bool)
        else:
            if not check[i-1] and not visit[i-1]:
                connect(i-1, bool)


n = int(input())
a = list(map(int, input().split()))
b = [[] for _ in range(n)]
for i in range(n):
    num, *lst = map(int, input().split())
    b[i] = lst
ans = sys.maxsize
for num in range(1, n//2+1):
    for case in combinations(range(n), num):
        check = [False]*n
        visit = [False]*n
        for node1 in case:
            check[node1] = True

        for i in range(n):
            if not check[i]:
                node2 = i
                break
        arr1, arr2 = list(), list()
        connect(node1, True)
        connect(node2, False)

        if len(arr1)+len(arr2) == n:
            sum_a, sum_b = 0, 0
            for i in arr1:
                sum_a += a[i]
            for i in arr2:
                sum_b += a[i]
            ans = min(ans, abs(sum_a-sum_b))
print(ans if ans != sys.maxsize else -1)
