def solve(x):
    length = 0
    for num in a:
        if num-x > 0:
            length += num-x
    return length


n, m = map(int, input().split())
a = list(map(int, input().split()))
left, right = 0, max(a)
ans = 0
while left <= right:
    mid = (left+right)//2
    if solve(mid) >= m:
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid-1
print(ans)
