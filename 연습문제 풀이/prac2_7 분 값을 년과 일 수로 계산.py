minute = eval(input('분에 대한 숫자를 입력하세요: '))

day = ((minute //60) //24)
year = day//365
day = day%365

print(minute,'분은 약 ',year,'년 ',day,'일 입니다.')

