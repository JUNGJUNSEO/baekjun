n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):

    if a[i] == b[i]:
        continue

    elif a[i] < b[i]:

        while a[i] < b[i]:
            ans += 1
            a[i] += 1

            for j in range(i + 1, n):

                if a[j] + 1 <= b[j]:
                    a[j] += 1
                else:
                    break

    else:

        while a[i] > b[i]:
            ans += 1
            a[i] -= 1

            for j in range(i + 1, n):

                if a[j] - 1 >= b[j]:
                    a[j] -= 1
                else:
                    break

print(ans)
