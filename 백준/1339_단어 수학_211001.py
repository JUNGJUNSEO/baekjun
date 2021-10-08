def back(m, num):
    global MAX
    if m == 0:
        ans = 0
        for s in a:
            cur = 0
            for w in s:
                cur = d[w] + cur*10
            ans += cur
        MAX = max(MAX, ans)
    for key in d.keys():
        if d[key] < 0:
            d[key] = num
            back(m-1, num-1)
            d[key] = -1


n = int(input())
a = [input() for _ in range(n)]
d = dict()
for i in range(n):
    for j in a[i]:
        d[j] = -1
MAX = 0
back(len(d), 9)
print(MAX)
