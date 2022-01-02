n = int(input())
members = list()
for order in range(n):
    (age, name) = input().split()
    members.append((int(age), name))
members = sorted(members, key=lambda x: x[0])
for member in members:
    print(f'{member[0]} {member[1]}')
