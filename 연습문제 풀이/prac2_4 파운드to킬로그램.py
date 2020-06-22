def pound_to_kilogram(pound):
    return pound* 0.454

pound = eval(input('파운드 값을 입력하세요:'))
print(pound,'파운드는 ',round(pound_to_kilogram(pound),3),'킬로그램입니다.')

