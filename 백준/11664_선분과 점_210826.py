from math import sqrt
ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())
mx, my, mz = (ax+bx)/2, (ay+by)/2, (az+bz)/2
print(mx, my, mz)
ans = sqrt((mx-cx)**2+(my-cy)**2+(mz-cz)**2)
print(ans)
