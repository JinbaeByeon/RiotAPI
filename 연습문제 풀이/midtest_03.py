MN = input("N,M: ").split()
N = int(MN[0])
M = int(MN[1])

score = [int(x) for x in input("점수: ").split()]
result =[]
for i in range(M):
    test = score[:]
    idx = [int(x)-1 for x in input("제외할 테스트 번호: ").split()]
    idx.sort()
    test.pop(idx[1])
    test.pop(idx[0])
    test.sort(reverse=True)
    result.append(test[0]+test[1])

for score in result:
    print(score)
# 55 70 80 50 90 75 70 90