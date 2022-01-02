p = input()
s = input()
ans = 0
for i in range(len(p)-len(s)+1):
    if p[i:i+len(s)] == s:
        ans = 1
print(ans)
