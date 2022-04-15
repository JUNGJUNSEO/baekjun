from collections import deque, defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):

    w = input().strip()
    k = int(input())
    storage = defaultdict(deque)
    ans = list()

    for i in range(len(w)):

        storage[w[i]].append(i)
        if len(storage[w[i]]) == k:
            ans.append(i - storage[w[i]].popleft() + 1)

    if ans:
        print(min(ans), max(ans))
    else:
        print(-1)
