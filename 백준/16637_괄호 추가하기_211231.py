def mul(lst):
    if len(lst) <= 3:
        return lst
    for i in range(len(lst)):
        if lst[i] == "*":
            return mul(
                lst[: i - 1] + [int(lst[i - 1]) * int(lst[i + 1])] + lst[i + 2 :]
            )


def cal(lst):
    lst = mul(lst)
    res = int(lst[0])
    for i in range(len(lst)):
        if lst[i] == "+":
            res += int(lst[i + 1])
        if lst[i] == "-":
            res -= int(lst[i + 1])
        if lst[i] == "*":
            res *= int(lst[i + 1])
    return res


def go(new, lst):
    global ans
    if len(lst) == 1:
        ans = max(ans, cal(new + lst))
        return
    if len(lst) == 0:
        ans = max(ans, cal(new))
        return

    for i in range(0, len(lst), 2):
        if i + 3 > len(lst):
            go(new + lst, [])
        elif i + 3 == len(lst):
            go(new + lst[0:i] + [cal(lst[i : i + 3])], [])
        elif i + 3 < len(lst):
            go(new + lst[0:i] + [cal(lst[i : i + 3])] + [lst[i + 3]], lst[i + 4 :])


n = int(input())
a = list(input())
ans = cal(a)
go([], a)
print(ans)
