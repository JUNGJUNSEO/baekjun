def solve(x):
    cnt = 0
    for num in a:
        cnt += num//x
    return cnt


k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]
left, right = 1, max(a)
while left <= right:
    mid = (left+right)//2
    if solve(mid) < n:
        right = mid-1
    else:
        ans = mid
        left = mid+1
print(ans)
