NUMBER_OF_CARDS = 52

import random

number = random.randint(0,NUMBER_OF_CARDS-1)

print("당신이 뽑은 카드는", end = " ")

if number //13 ==0:
    print("크로바",end=" ")
elif number //13 ==1:
    print("다이아몬드",end=" ")
elif number //13 ==2:
    print("하트",end=" ")
elif number //13 ==3:
    print("스페이드",end=" ")

if number % 13 == 0:
    print("A 입니다.")
elif number % 13 == 12:
    print("K 입니다.")
elif number % 13 == 11:
    print("Q 입니다.")
elif number % 13 == 10:
    print("J 입니다.")
else:
    print(number%13+1," 입니다.")
print(number)
