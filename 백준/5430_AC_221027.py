from collections import deque

t = int(input())

for _ in range(t):

    p = list(input())
    n = int(input())
    a = list(input()[1:-1].split(','))
    a = deque(a)
    if n == 0:
        a = []
    cnt = 0
    check = False

    for w in p:

        if w == 'R':
            cnt += 1
        else:
            if not a:
                print('error')
                check = True
                break

            if cnt % 2 == 0:
                a.popleft()
            else:
                a.pop()

    if not check:

        a = list(a)

        if cnt % 2 == 0:
            print('[' + ','.join(a) + ']')
        else:
            print('[' + ','.join(a[::-1]) + ']')
