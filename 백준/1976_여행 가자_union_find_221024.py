def find_parent(x):

    if parent[x] != x:
        return find_parent(parent[x])
    return x


def union_parent(a, b):

    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
parent = list(range(n))

for x in range(n):
    for y, num in enumerate(list(map(int, input().split()))):
        if num == 1:
            union_parent(x, y)

for i in range(n):
    parent[i] = find_parent(i)

ans = 'YES'
par = -1

for p in list(map(int, input().split())):
    if par < 0:
        par = parent[p-1]
    if par != parent[p-1]:
        ans = 'NO'
        break

print(ans)
