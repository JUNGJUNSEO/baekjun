a = input()


def go(index, m):
    global ans
    if m == 0:
        ans += 1
        return

    if a[index] == "d":
        for i in range(10):
            if not s or s[-1] != i:
                s.append(i)
                go(index + 1, m - 1)
                s.pop()
    if a[index] == "c":
        for i in range(26):
            if not s or s[-1] != chr(i + 65):
                s.append(chr(i + 65))
                go(index + 1, m - 1)
                s.pop()


ans = 0
s = list()
go(0, len(a))
print(ans)
