def f(price,percentage):
    tip = price * percentage/100
    return tip

price =eval(input('소계: '))
tip = f(price,eval(input('팁 비율: ')))

print('팁은 ',round(tip,2),'이고 총액은 ',round(price+tip,2),'입니다.')
