def calc(n):
    l = len(str(n))
    cnt = 0
    for i in range(1, l):
        cnt += 9*10**(i-1)*i
    cnt += (n+1-10**(l-1))*l
    return cnt


def go(n, k):
    if calc(n) < k:
        return -1
    left, right = 1, n
    while left <= right:
        mid = (left+right)//2
        if calc(mid) < k:
            left = mid+1
        else:
            ans = mid
            right = mid-1
    s = str(ans)
    return s[len(s)-(calc(ans)-k)-1]


n, k = map(int, input().split())
print(go(n, k))
