n = int(input())
a = list(map(int, input().split()))
lst = list()
for i in range(1, 1 << n):
    s = 0
    for j in range(n):
        if i & (1 << j) > 0:
            s += a[j]
    lst.append(s)
lst.sort()
ans = max(lst) + 1
for index, element in enumerate(set(lst)):
    if index + 1 != element:
        ans = index + 1
        break
print(ans)
