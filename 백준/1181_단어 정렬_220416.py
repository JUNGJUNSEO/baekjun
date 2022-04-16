import sys
input = sys.stdin.readline

n = int(input())
a = [input().strip() for _ in range(n)]
lst = list(set(a))
lst.sort()
lst.sort(key=len)

for word in lst:
    print(word)
