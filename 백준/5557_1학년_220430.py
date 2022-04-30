from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)

for i in range(n-1):

    if not d:
        d[a[i]] = 1
        continue

    new_dict = defaultdict(int)
    for key in d.keys():
        for s in [-1, 1]:
            if 0 <= key+a[i]*s <= 20:
                new_dict[key+a[i]*s] += d[key]

    d = new_dict
    print(d)
print(d[a[n-1]])
