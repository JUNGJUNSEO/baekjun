from collections import deque


def solve():
    cnt = 0

    for num in order:
        while q:
            val, idx = q.popleft()
            if val == num:
                cnt += 1
                if idx == m:
                    return cnt
                break
            else:
                q.append([val, idx])


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    order = sorted(a, reverse=True)
    a = [[val, idx] for idx, val in enumerate(a)]
    q = deque(a)
    print(solve())
