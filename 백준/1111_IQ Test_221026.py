def check(a, b):

    for i in range(n-1):
        if s[i] * a + b != s[i+1]:
            return False
    return True


n = int(input())
s = list(map(int, input().split()))

if n == 1:

    print('A')

elif n == 2:

    if s[0] == s[1]:
        print(s[0])
    else:
        print('A')

elif n >= 3:

    if s[0] - s[1] == 0:
        a = 0
    else:
        a = (s[1] - s[2]) // (s[0] - s[1])

    b = s[1] - a * s[0]

    if not check(a, b):
        print('B')
    else:
        print(s[n-1]*a + b)
