n = int(input())
scores = []
for _ in range(n):
    [name, kor, eng, math] = input().split()
    scores.append([name, int(kor), int(eng), int(math)])
scores = sorted(scores, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for score in scores:
    print(score[0])
