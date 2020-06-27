
def Small_Straight(ai):
    dice = ai[:]
    dice.sort()

    num = dice[0]
    cnt = 0
    for i in range(len(ai)):
        if dice[i] == num:
            num += 1
            cnt += 1
        elif cnt != 4 and dice[i] != num - 1:
            num = dice[i] + 1
            cnt = 1

    if cnt >= 4:
        print("YES")
    else:
        print("NO")

numbers=[]
while len(numbers) < 4:
    numbers = input("5개의 주사위 숫자 입력: ").split()
    if len(numbers) < 4:
        print("오류. 4개 이상의 주사위를 입력하세요.")

ai = [int(x) for x in numbers]

Small_Straight(ai)