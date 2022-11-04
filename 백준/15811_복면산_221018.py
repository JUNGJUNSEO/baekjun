from itertools import permutations
import sys
input = sys.stdin.readline


def str2num(w):

    num = 0

    for c in w:
        num = num*10 + d[c]

    return num


def solve(case):
    for i in range(l):
        d[s[i]] = case[i]

    n1 = str2num(w1)
    n2 = str2num(w2)
    n3 = str2num(w3)

    return n1+n2 == n3


w1, w2, w3 = map(list, input().split())
s = set(w1+w2+w3)
s = list(s)
d = {}
l = len(s)
ans = 'NO'

for case in permutations(list(range(10)), l):
    if l > 10:
        break
    if solve(case):
        ans = 'YES'
        break
print(ans)
