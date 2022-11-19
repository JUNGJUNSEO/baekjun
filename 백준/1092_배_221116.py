import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

ans = 0

while b:

    if b[0] > a[0]:
        ans = -1
        break

    for i in range(n):
        for j in range(len(b)):

            if a[i] >= b[j]:
                b.remove(b[j])
                break

    ans += 1

print(ans)
