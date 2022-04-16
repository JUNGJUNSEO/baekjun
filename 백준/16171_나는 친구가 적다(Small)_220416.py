s = input()
k = input()

lst = ""
for a in s:
    if 0 <= ord(a)-ord('a') < 26 or 0 <= ord(a)-ord('A') < 26:
        lst += a

print(1 if k in lst else 0)
