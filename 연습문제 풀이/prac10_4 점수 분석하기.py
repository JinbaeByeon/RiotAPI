s= input("정수를 입력하세요: ")
items = s.split()
scores = [int(x) for x in items]

average = 0
cnt = 0
for i in scores:
    cnt += 1
    average += i

average /= cnt

cnt = [0]*2
for i in scores:
    if i >= average:
        cnt[0]+=1
    else:
        cnt[1] += 1

print(average,'이상: ',cnt[0]," 평균 미만: ", cnt[1])
    
