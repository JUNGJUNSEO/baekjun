n = int(input())
a = list(int(input()) for _ in range(n))
ans = 1
for i in range(n-1):
    if a[i] > a[i+1]:
        ans += 1
    elif a[i] > a[i+1]
print(ans)
