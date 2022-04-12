from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
d = defaultdict(int)
files = [input() for _ in range(n)]
for file in files:
    d[file.split('.')[1].strip()] += 1
print(d)
for name in sorted(d):
    print(name, d[name])
