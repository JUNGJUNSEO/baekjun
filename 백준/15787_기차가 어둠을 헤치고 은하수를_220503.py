import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = [0]*n

for _ in range(m):
    num, *order = map(int, input().split())
    if num == 1:
        i, x = order
        t[i-1] |= 1 << x-1
    if num == 2:
        i, x = order
        t[i-1] &= ~(1 << x-1)
    if num == 3:
        i = order[0]
        t[i-1] <<= 1
        t[i-1] &= ~(1 << 20)
    if num == 4:
        i = order[0]
        t[i-1] >>= 1

print(len(set(t)))
