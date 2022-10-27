Inf = int(1e9)
d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

new_oven = [0] * d
s = Inf

for idx, o in enumerate(oven):

    if s > o:
        s = o

    new_oven[idx] = s


idx = d
ans = 0

for i in range(n):

    while True:

        idx -= 1

        if idx < 0:
            print(0)
            exit()

        if pizza[i] <= new_oven[idx]:
            ans = idx+1
            break

print(ans)
