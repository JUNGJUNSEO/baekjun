def mul(lst):
    for i in range(len(lst)):
        if lst[i] == "*":
            if i + 2 >= len(lst):
                lst = lst[: i - 1] + [int(lst[i - 1]) * int(lst[i + 1])]
            else:
                lst = lst[: i - 1] + [int(lst[i - 1]) * int(lst[i + 1])] + lst[i + 2 :]
            return mul(lst)
    return lst


def cal(lst):
    lst = mul(lst)
    res = int(lst[0])
    for i in range(len(lst)):
        if lst[i] == "+":
            res += int(lst[i + 1])
        if lst[i] == "-":
            res -= int(lst[i + 1])

    return res


def go(new, lst):
    global ans
    l = len(lst)
    if l == 1:
        ans = max(ans, cal(new + lst))
        return
    if l == 0:
        ans = max(ans, cal(new))
        return

    for i in range(0, l, 2):
        if i + 3 > l:
            go(new + lst, [])
        elif i + 3 == l:
            go(new + lst[0:i] + [cal(lst[i : i + 3])], [])
        elif i + 3 < l:
            go(new + lst[0:i] + [cal(lst[i : i + 3])] + [lst[i + 3]], lst[i + 4 :])


n = int(input())
a = list(input())
ans = cal(a)
go([], a)
print(ans)
