

N = eval(input("컵의 교체 횟수: "))

a=[]
b=[]
g=[]
for i in range(N):
    line = input("(a,b,g): ").split()
    a.append(int(line[0]))
    b.append(int(line[1]))
    g.append(int(line[2]))

max_score = 0
for target in range(1,4):
    score = 0
    for i in range(N):
        if a[i] == target:
            target = b[i]
        elif b[i] == target:
            target = a[i]
        if target == g[i]:
            score += 1
    if max_score < score:
        max_score = score


print(max_score)
