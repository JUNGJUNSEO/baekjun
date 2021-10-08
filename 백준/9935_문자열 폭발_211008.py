s = input()
a = list(input())
l = len(a)
t = []
for w in s:
    t.append(w)
    if t[-l:] == a:
        for _ in range(l):
            t.pop()
if not t:
    print('FRULA')
else:
    print(''.join(map(str, t)))
