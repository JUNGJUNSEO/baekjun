import math
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0

for student in a:
    # 총감독관, 부감독관이 포함된 경우.
    cnt_dir = 1
    if student-b > 0:
        cnt_dir += math.ceil((student-b) / c)

    ans += cnt_dir

print(ans)
