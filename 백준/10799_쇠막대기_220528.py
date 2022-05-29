import sys
input = sys.stdin.readline

a = list(input())
s = list()
ans = 0

for i in range(len(a)):
    if a[i] == ')':
        cnt = 0
        while True:
            x = s.pop()
            if x == '(':
                if cnt > 0:
                    ans += cnt+1
                    s.append(cnt)
                else:
                    s.append(1)
                break
            else:
                cnt += x
    else:
        s.append(a[i])

print(ans)
