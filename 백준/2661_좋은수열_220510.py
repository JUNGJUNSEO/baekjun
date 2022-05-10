def solve(s, cnt):

    if cnt == n:
        print(s)
        exit()

    for num in [1, 2, 3]:
        temp = s+str(num)
        check = True

        for i in range(1, len(temp)+1):
            if 2*i <= len(temp) and temp[-i:] == temp[-(2*i):-i]:
                check = False
                break

        if check:
            solve(temp, cnt+1)


n = int(input())
solve('', 0)
