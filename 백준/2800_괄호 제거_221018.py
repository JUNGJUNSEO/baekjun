a = input()
l = len(a)
q = []
cnt = 0
index = [-1]*l

for idx, ch in enumerate(a):
    if ch == '(':
        q.append(idx)
    elif ch == ')':
        x = q.pop()
        index[x] = index[idx] = cnt
        cnt += 1

choose = [0]*cnt


def func(i):

    if i == cnt:
        if sum(choose) < cnt:
            res = []
            for idx, ch in enumerate(a):
                if index[idx] < 0 or choose[index[idx]] == 1:
                    res.append(ch)
            ans.append(''.join(res))
        return

    choose[i] = 1
    func(i+1)
    choose[i] = 0
    func(i+1)


ans = []
func(0)
ans = sorted(set(ans))
for a in ans:
    print(a)
