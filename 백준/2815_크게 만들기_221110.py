n, k = map(int, input().split())
c = k
a = list(map(int, input()))
s = []

for i in range(n):
    while c > 0 and s and s[-1] < a[i]:
        s.pop()
        c -= 1
    s.append(a[i])

print(''.join(map(str, s[:n-k])))
