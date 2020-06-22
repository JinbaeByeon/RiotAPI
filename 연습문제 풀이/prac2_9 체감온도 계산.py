def twc(ta,v):
    return 35.74 + 0.6215*ta - 35.75*v**0.16 + 0.4275*ta*v**0.16

ta = eval(input('화씨 -58°F 와 41°F 사이의 온도를 입력하세요: '))
v = eval(input('풍속을 시간 당 마일 단위로 입력하세요: '))
print('체감온도는 ',twc(ta,v),' 입니다')
