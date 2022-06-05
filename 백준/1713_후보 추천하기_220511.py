import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
a = list(map(int, input().split()))
photo = dict()

for i in range(m):

    if a[i] in photo:
        photo[a[i]][0] += 1
    else:
        if len(photo) == n:
            del photo[a[sorted(photo.values())[0][1]]]
        photo[a[i]] = [1, i]

print(' '.join(map(str, sorted(photo.keys()))))
