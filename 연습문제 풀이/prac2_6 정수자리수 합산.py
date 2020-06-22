number = eval(input('0과 1000 사이의 숫자를 입력하세요: '))
sum_num = 0
while(number != 0):
    sum_num = sum_num + number %10
    number = number//10

print('이 자릿수들의 합은 ',sum_num,' 입니다.')
