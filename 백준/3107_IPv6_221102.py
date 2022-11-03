a = input()
a = a.split(':')

cnt = 0

for i in range(len(a)):

    if a[i]:
        cnt += 1

ans = ''
check = True

for i in range(len(a)):

    if not a[i]:
        if check:
            for _ in range(8-cnt):
                ans += a[i].zfill(4) + ':'

            check = False
    else:
        ans += a[i].zfill(4) + ':'

print(ans[:-1])
