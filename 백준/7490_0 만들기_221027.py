def solve(num, res):

    if num == n:
        if eval(res.replace(' ', '')) == 0:
            print(res)

        return

    solve(num+1, res + ' ' + str(num+1))
    solve(num+1, res + '+' + str(num+1))
    solve(num+1, res + '-' + str(num+1))


for _ in range(int(input())):

    n = int(input())
    solve(1, '1')
    print()
