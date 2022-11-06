from collections import deque
n, w, l = map(int, input().split())
a = list(map(int, input().split()))
s = deque([0]*w)
idx = 0
ans = 1

while True:

    s.popleft()

    if sum(s) + a[idx] <= l:
        s.append(a[idx])
        idx += 1
    else:
        s.append(0)

    if idx == n:
        break

    ans += 1

while sum(s):
    s.append(0)
    s.popleft()
    ans += 1

print(ans)
