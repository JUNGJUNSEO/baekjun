import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
cnt, ans_cnt, ans = 1, 1, a[0]
for i in range(n-1):
    if a[i] == a[i+1]:
        cnt += 1
    else:
        cnt = 1
    if cnt > ans_cnt:
        ans_cnt = cnt
        ans = a[i]
print(ans)
