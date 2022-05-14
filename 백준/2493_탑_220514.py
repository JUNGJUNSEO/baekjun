n = int(input())
a = list(map(int, input().split()))
idx = list()
ans = [0]*n

for i in range(len(a)-1, -1, -1):

    while idx:
        if a[i] >= a[idx[-1]]:
            ans[idx.pop()] = i+1
        else:
            break
    idx.append(i)

print(' '.join(map(str, ans)))
