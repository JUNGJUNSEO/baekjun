n = int(input())
a = list(map(int, input().split()))
a.sort()

left, right = 0, n-1
ans = abs(a[left]+a[right])

ans_left, ans_right = a[left], a[right]

while left != right:

    SUM = a[left]+a[right]
    if abs(SUM) < ans:
        ans = abs(SUM)
        ans_left, ans_right = a[left], a[right]

    if SUM > 0:
        right -= 1
    else:
        left += 1

print(ans_left, ans_right)
