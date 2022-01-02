from collections import deque

f, s, g, u, d = map(int, input().split())
ans = [0]*(f+1)
q = deque()
q.append(s)
while q:
    x = q.popleft()
    for button in [u, -d]:
        if button and 1 <= x+button <= f:
            if not ans[x+button]:
                ans[x+button] = ans[x]+1
                q.append(x+button)
if s == g:
    print(0)
else:
    if ans[g] == 0:
        print('use the stairs')
    else:
        print(ans[g])
