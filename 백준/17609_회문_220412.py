def go(left, right, ans):

    if ans == 2:
        return 2

    while left < right:

        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            return min(go(left+1, right, ans + 1), go(left, right-1, ans + 1))

    return ans


n = int(input())
for _ in range(n):
    a = input()
    print(go(0, len(a)-1, 0))
