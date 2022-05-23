from collections import defaultdict
n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a += a
left, right = 0, 0
ans = 0
length = len(a)
d = defaultdict(int)
s = set()

while right < length:

    if right-left < k:
        d[a[right]] += 1
        s.add(a[right])
        right += 1
    else:
        if c not in s:
            ans = max(ans, len(s)+1)
        else:
            ans = max(ans, len(s))
        d[a[left]] -= 1
        if d[a[left]] == 0:
            s.remove(a[left])
        left += 1

print(ans)
