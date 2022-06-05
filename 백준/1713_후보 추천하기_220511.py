from collections import defaultdict
import sys
input = sys.stdin.readline


def delete(MIN):
    lst = list()
    for key, value in student.items():
        if value == MIN:
            lst.append([order[key], key])
    lst.sort()

    del student[lst[0][1]]
    del order[lst[0][1]]


n = int(input())
m = int(input())
a = list(map(int, input().split()))
student = defaultdict(int)
order = dict()

for i in range(m):
    if len(student) < n:
        student[a[i]] += 1
        if a[i] not in order:
            order[a[i]] = i
    else:
        if a[i] in student:
            student[a[i]] += 1
        else:
            MIN = min(student.values())
            delete(MIN)
            student[a[i]] += 1
            order[a[i]] = i

print(' '.join(map(str, sorted(student.keys()))))
