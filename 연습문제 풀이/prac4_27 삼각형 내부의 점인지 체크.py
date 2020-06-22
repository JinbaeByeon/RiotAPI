x,y = eval(input("점의 x와 y 좌표값을 입력하세요: "))

if y < -x/2+100 and x> 0 and y>0:
    print("점은 삼각형의 내부에 있습니다.")
else:
    print("점은 삼각형의 내부에 있지 않습니다.")
