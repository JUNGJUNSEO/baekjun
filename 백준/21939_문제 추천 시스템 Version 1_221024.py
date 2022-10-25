from heapq import heappop, heappush


def add(p, l):

    heappush(max_heap, [-l, -p])
    heappush(min_heap, [l, p])


max_heap = []
min_heap = []
solved = [0] * (10 ** 5 + 1)
n = int(input())

for _ in range(n):
    p, l = map(int, input().split())
    add(p, l)

m = int(input())

for _ in range(m):

    o = input().split()

    if o[0] == 'recommend':
        if o[1] == '1':
            while True:
                _, p = max_heap[0]

                if solved[-p]:
                    heappop(max_heap)
                    solved[-p] -= 1
                else:
                    print(-p)
                    break

        else:
            while True:
                _, p = min_heap[0]

                if solved[p]:
                    heappop(min_heap)
                    solved[p] -= 1
                else:
                    print(p)
                    break

    elif o[0] == 'add':
        p, l = map(int, o[1:])
        add(p, l)

    elif o[0] == 'solved':
        p = int(o[1])
        solved[p] = 1
