def Small_Straight(ai):
    dice = ai[:]
    dice.sort()
    
    num = dice[0]
    cnt = 0
    for i in range(5):
        if dice[i] == num:
            num += 1
            cnt += 1
        elif cnt != 4 and dice[i] != num-1 :
            num = dice[i]+1
            cnt = 1


    if cnt >= 4:
        print("YES")
    else:
        print("NO")


ai = [int(x) for x in input("5개의 주사위 숫자 입력: ").split()]

Small_Straight(ai)