from itertools import permutations

a, b = map(int, input().split())

lst_a = list(map(int, str(a)))
ans = -1
for item in permutations(lst_a, len(lst_a)):
    if item[0] == 0:
        continue
    res = int("".join(map(str, item)))
    if res - b < 0:
        ans = max(ans, res)
print(ans)
