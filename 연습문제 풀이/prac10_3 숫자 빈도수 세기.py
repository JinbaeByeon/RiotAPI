s = input("1과 100 사이의 정수를 입력하세요: ")
items = s.split()
numbers = [int(x) for x in items]

cnt = [0] * 100

for value in numbers:
    if value <= 100 and value >=1:
        cnt[value-1] += 1

for i in range(100):
    if cnt[i] >0: print(i+1," - ",cnt[i],"번 나타납니다.")
