a, b, c, x, y = map(int, input().split())
if a+b < 2*c:
    ans = a*x + b*y
else:
    ans = c*2*max(x, y)
    m = min(x, y)
    if x > y:
        ans = min(ans, a*(x-m) + c*2*m)
    else:
        ans = min(ans, b*(y-m) + c*2*m)
print(ans)
