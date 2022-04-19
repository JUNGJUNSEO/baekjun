from collections import defaultdict
import sys
input = sys.stdin.readline

trees = defaultdict(int)
cnt = 0
while True:
    tree = input().strip()
    if not tree:
        break
    cnt += 1
    trees[tree] += 1

for name, num in sorted(trees.items()):
    print("%s %.4f" % (name, num/cnt*100))
