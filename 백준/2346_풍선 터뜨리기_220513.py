from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))

while q:
    idx, num = q.popleft()
    print(idx+1, end=' ')
    if num > 0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)
